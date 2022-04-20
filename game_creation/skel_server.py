import builtins
from enum import Enum
from server_info import ServerData
from twisted.internet import reactor, endpoints
from twisted.internet.protocol import ServerFactory, Protocol
# from configuration_protocol import ServerConfig
import shared_directory.data_format as form
import s_message_handler as handler
import session
import json, pika, logging


# noinspection PyArgumentList
class MainServer(Protocol):
    format = form.decode_format()

    def connectionMade(self):
        pass

    def login(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.LOGIN_RESPONSE, data)
        self.tcp_send_data(d)

    def invalid_session(self):
        d = self.format_send_data(form.ServerRequestTypeEnum.INVALID_SESSION)
        self.tcp_send_data(d)

    def send_create_game(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.CREATE_GAME_RESPONSE, data)
        self.tcp_send_data(d)

    def send_join_game(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.JOIN_GAME_RESPONSE, data)
        self.tcp_send_data(d)

    def send_ready_game(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.READY_GAME_RESPONSE, data)
        self.tcp_send_data(d)

    def send_aggregate_lobby(self):
        all_games = handler.aggregate_lobby_list()
        d = self.format_send_data(form.ServerRequestTypeEnum.UPDATE_EVERY_GAME_LIST, all_games)
        self.tcp_send_data(d)
        self.queue_message(form.exchange_name(), '', d)

    def send_aggregate_player_list(self, game_id):
        players = handler.aggregate_player_list(game_id)
        d = self.format_send_data(form.ServerRequestTypeEnum.UPDATE_PLAYER_LIST, players)
        self.queue_message(form.game_exchange_name(), game_id, d)
        self.tcp_send_data(d)

    def send_start_game(self, game_id, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.READY_GAME_RESPONSE, data)
        self.queue_message(form.game_exchange_name(), game_id, d)

    def send_new_bet(self, game_id):
        pass

    def send_bet_response(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.BET_RESPONSE, data)
        self.tcp_send_data(d)

    def send_cards(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.CARDS, data)
        self.tcp_send_data(d)

    def send_new_cards(self, data):
        d = self.format_send_data(form.ServerRequestTypeEnum.REPLACED_CARDS, data)
        self.tcp_send_data(d)

    def send_signal_start(self):
        ServerData.logger.info('Signal to start')
        d = self.format_send_data(form.ServerRequestTypeEnum.SIGNAL_START)
        self.tcp_send_data(d)

    def signal_state_change(self, game_id, state):
        d = self.format_send_data(form.ServerRequestTypeEnum.STATE_CHANGE, state)
        self.queue_message(form.game_exchange_name(), game_id, d)

    def send_winners(self, winners, game_id):
        d = self.format_send_data(form.ServerRequestTypeEnum.GAME_WINNERS, winners)
        self.queue_message(form.game_exchange_name(), game_id, d)

    @staticmethod
    def format_send_data(request_type, data=None):
        req = form.ServerRequestHeader()
        req.request_type = request_type
        if data:
            try:
                if isinstance(data, Enum):
                    req.data = data
                else:
                    req.data = data.__dict__
            except builtins.AttributeError:
                req.data = data
        else:
            req.data = ''
        print(request_type.name)
        ServerData.logger.info(req.__dict__)
        s = json.dumps(req.__dict__)
        return s

    def tcp_send_data(self, message):
        self.transport.write(f'{message}\r'.encode(self.format))

    @staticmethod
    def queue_message(exchange, routing_key, message):
        print(f'exchange: {exchange}'
f'routing key: {routing_key}'
f'message: {message}')
        x = MessageQueue(exchange=exchange, routing_key=routing_key)
        x.send_message(message=message, routing_key=routing_key)
        x.close_connection()

    def dataReceived(self, data: bytes):
        sp_data = data.decode(self.format).split('\r')
        remove = [x for x in sp_data if x]
        for d in remove:
            print(d)
            messages = form.ClientRequestHeader(d)
            if messages.request_type == form.ClientRequestTypeEnum.LOGIN_REQUEST:
                server_data = handler.handle_login_requests(messages.data)
                self.login(server_data)
                self.send_aggregate_lobby()
            # Validate session updates the activity timer. Therefore, no need to call it for the keep alive
            elif session.Session.validate_session(messages.session_id):
                match messages.request_type:
                    case form.ClientRequestTypeEnum.KEEP_ALIVE:
                        print(f'keep alive message received from {messages.session_id}: {messages.data}')
                    case form.ClientRequestTypeEnum.LOGOUT_REQUEST:
                        session.Session.delete_session(messages.session_id)
                    case form.ClientRequestTypeEnum.CREATE_GAME:
                        list_d = handler.handle_create_game(messages.data, messages.session_id)
                        server_data, game_id = list_d
                        self.send_create_game(server_data)
                        self.send_aggregate_lobby()
                        self.send_aggregate_player_list(game_id)
                    case form.ClientRequestTypeEnum.JOIN_GAME:
                        server_data, game_id = handler.handle_join_game(messages.data, messages.session_id)
                        self.send_join_game(server_data)
                        self.send_aggregate_player_list(game_id)
                    case form.ClientRequestTypeEnum.READY_GAME:
                        server_data, game_id = handler.handle_ready_game(messages.data, messages.session_id)
                        self.send_ready_game(server_data)
                        self.send_aggregate_player_list(game_id)
                    case form.ClientRequestTypeEnum.START_GAME:
                        server_data, game_id = handler.handle_start_game(messages.data, messages.session_id)
                        self.send_start_game(data=server_data, game_id=game_id)
                    case form.ClientRequestTypeEnum.SEND_BET:
                        ServerData.logger.info('Bet received')
                        server_data, game_id, complete = handler.handle_input_bet(messages.data, messages.session_id)
                        self.send_bet_response(server_data)
                        self.send_new_bet(game_id)
                        if complete:
                            self.signal_state_change(game_id=game_id, state=form.GameState.CARD_CHANGING)
                    case form.ClientRequestTypeEnum.REQUEST_CARDS:
                        server_data = handler.get_cards(messages.data, messages.session_id)
                        self.send_cards(server_data)
                    case form.ClientRequestTypeEnum.SEND_CARDS:
                        server_data, game_id, complete = handler.replace_cards(messages.data, messages.session_id)
                        self.send_new_cards(server_data)
                        if complete:
                            winners = handler.calculate_game_score(game_id)
                            self.send_winners(winners, game_id)
                    case form.ClientRequestTypeEnum.SIGNAL_START:
                        ServerData.logger.info('Received signal start')
                        self.send_signal_start()
                    case _:
                        pass

            else:
                print('Invalid session request')
                self.invalid_session()


class ServerProtocol(ServerFactory):
    def buildProtocol(self, addr):
        return MainServer()


class MessageQueue:
    def __init__(self, exchange, routing_key=''):
        self.exchange = exchange
        self.routing_key = routing_key
        my_url = form.message_url()


        self.connection = pika.BlockingConnection(pika.URLParameters(url=my_url))
        self.channel = self.connection.channel()

        # self.channel.queue_declare(queue=queue_name, durable=True, exclusive=False, auto_delete=False)

    def construct_message(self):
        pass

    def send_message(self, message, routing_key=''):
        self.channel.basic_publish(self.exchange, body=message, routing_key=routing_key)

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    import colouredlogs

    ServerData.logger = logging.getLogger('Main')
    colouredlogs.format('[%(hostname)s] %(asctime)s %(message)s')

    colouredlogs.install(logger=ServerData.logger)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    # message_queue = MessageQueue(exchange='gameserver.broadcast')
    endpoint.listen(ServerProtocol())
    reactor.run()

