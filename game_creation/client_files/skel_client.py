import builtins, logging, json, pika
'''
from twisted.internet.defer import Deferred
from twisted.internet.threads import deferToThread
'''
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
from game_creation.shared_directory import data_format as form
from client_data import ClientInfo

decode_type = form.decode_format()


# noinspection PyArgumentList
class MainClient(Protocol):
    format = decode_type

    def __init__(self):
        self.loop: LoopingCall = LoopingCall(self.send_keep_alive)
        self.lobby_mq: MessageQueue = None
        self.game_mq: MessageQueue = None

    def connectionMade(self):
        # Do we want the client to be auto logged in?
        # Do we want to save the login details if they have logged in before?
        pass

    def connectionLost(self, reason):
        print('disconnecting')

    def send_login(self, username, password):
        x = form.ClientLoginRequest()
        x.username = username
        x.password = password
        x.version = form.version_number()
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        ClientInfo.logger.info('Send login')
        self.transport.write(f'{s}\r'.encode(self.format))

    def send_logout(self):
        ClientInfo.logger.info('Send logout')
        self.lobby_mq.stop_consumption()
        self.format_send_data(form.ClientRequestTypeEnum.LOGOUT_REQUEST)

    def create_game(self, name, game_type, password=''):
        user_data = form.ClientCreateGame()
        user_data.game_type = game_type
        user_data.game_name = name
        user_data.password = password
        self.format_send_data(form.ClientRequestTypeEnum.CREATE_GAME, user_data)

    def join_game(self, game_id, password=''):
        user_data = form.ClientJoinGame()
        user_data.game_id = game_id
        user_data.password = password
        self.format_send_data(form.ClientRequestTypeEnum.JOIN_GAME, user_data)

    def ready_game(self, game_id, ready_type):
        user_data = form.ClientReadyGame()
        user_data.game_id = game_id
        user_data.request = ready_type
        self.format_send_data(form.ClientRequestTypeEnum.READY_GAME, user_data)

    def start_game(self):
        user_data = form.ClientStartGame()
        user_data.game_id = ClientInfo.game_id
        self.format_send_data(form.ClientRequestTypeEnum.START_GAME, user_data)

    def send_bet(self, amount):
        user_data = form.ClientSendBet()
        user_data.bet = amount
        user_data.game_id = ClientInfo.game_id
        self.format_send_data(form.ClientRequestTypeEnum.SEND_BET, user_data)

    def request_cards(self):
        self.format_send_data(form.ClientRequestTypeEnum.REQUEST_CARDS, ClientInfo.game_id)

    def format_send_data(self, request_type: form.ClientRequestTypeEnum, data=None):
        req = form.ClientRequestHeader()
        req.request_type = request_type
        req.session_id = ClientInfo.session_id
        if data:
            try:
                req.data = data.__dict__
            except builtins.AttributeError:
                req.data = data
        else:
            req.data = ''
        s = json.dumps(req.__dict__)
        ClientInfo.logger.info(f'{request_type.name}')
        self.transport.write(f'{s}\r'.encode(self.format))

    def dataReceived(self, data: bytes):
        listed_data = self.decode_data(data)
        for json_data in listed_data:
            ClientInfo.logger.debug(f'{json_data}')
            message = form.ServerRequestHeader(json_data)
            match message.request_type:
                case form.ServerRequestTypeEnum.LOGIN_RESPONSE:
                    ClientInfo.logger.info('Handling login')
                    self.handle_login_response(message.data)
                case form.ServerRequestTypeEnum.INVALID_SESSION:
                    # Stop keep alive function
                    ClientInfo.logger.error('Invalid session. Log in')
                    self.loop.stop()
                case form.ServerRequestTypeEnum.CREATE_GAME_RESPONSE:
                    self.handle_create_game_response(message.data)
                case form.ServerRequestTypeEnum.JOIN_GAME_RESPONSE:
                    self.handle_join_game_response(message.data)
                case form.ServerRequestTypeEnum.UPDATE_EVERY_GAME_LIST:
                    ClientInfo.main_gui.set_game_list(message.data)
                case form.ServerRequestTypeEnum.UPDATE_PLAYER_LIST:
                    ClientInfo.main_gui.set_player_list(message.data)
                case form.ServerRequestTypeEnum.READY_GAME_RESPONSE:
                    self.handle_ready_game_response(message.data)
                case form.ServerRequestTypeEnum.CARDS:
                    self.handle_cards(message.data)
                case form.ServerRequestTypeEnum.BET_RESPONSE:
                    self.handle_bet_response(message.data)
                case _:
                    # Invalid command
                    pass

    def decode_data(self, data):
        sp_data = data.decode(self.format).split('\r')
        return [x for x in sp_data if x]

    def handle_login_response(self, data):
        response_data = form.ServerLoginResponse(data)
        ClientInfo.logger.info(response_data.message)
        if response_data.response_code == form.LoginResponseEnum.SUCCESS:
            ClientInfo.set_login_values(response_data.username, response_data.keep_alive,
                                        response_data.session_id)
            ClientInfo.valid_session = True
            self.loop.start(response_data.keep_alive)
            # reactor.callFromThread(self.start_keep_alive, response_data.keep_alive)
            ClientInfo.logger.info('Running message queue')
            self.lobby_mq = MessageQueue(queue_name=f'gameserver.{response_data.username}.{response_data.session_id}',
                                         exchange=form.exchange_name())
            self.lobby_mq.set_consume()
            reactor.callInThread(self.lobby_mq.start_consumption)
            ClientInfo.logger.info('Message queue has successfully been added to the thread')
            ClientInfo.login_gui.login_response_success()
            ClientInfo.main_gui.change_screens(form.MenuScreenEnums.GAME_LIST)
            # self.create_game()
        elif response_data.response_code == form.LoginResponseEnum.ERROR:
            # User must re-input
            # self.send_login()
            ClientInfo.login_gui.login_response_failed()
            pass
        else:
            raise RuntimeError

    def send_keep_alive(self):
        self.format_send_data(form.ClientRequestTypeEnum.KEEP_ALIVE, ClientInfo.username)

    def handle_create_game_response(self, data):
        response_data = form.ServerCreateGame(data)
        if response_data.response_code == form.CreateGameEnum.SUCCESS:
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.SUCCESS.name}')
            ClientInfo.game_id = response_data.game_id
            ClientInfo.game_owner = True
            # Creator listens in on Game Queue
            self.game_mq = MessageQueue(queue_name=f'gameserver.{ClientInfo.username}.playing.game.{response_data.game_id}',
                                         exchange=form.game_exchange_name(), routing_key=response_data.game_id)
            self.game_mq.set_consume()
            reactor.callInThread(self.game_mq.start_consumption)
            ClientInfo.logger.info(f'Listening to Game Queue with Queue Name {self.game_mq.queue_name}')
            ClientInfo.create_game_gui.create_response_success()
            ClientInfo.main_gui.change_screens(form.MenuScreenEnums.WAITING_ROOM)
        elif response_data.response_code == form.CreateGameEnum.NAME_ERROR:
            # Popup
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.NAME_ERROR.name}')
        elif response_data.response_code == form.CreateGameEnum.ALREADY_CREATED_GAME:
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.ALREADY_CREATED_GAME.name}')
        else:
            raise RuntimeError

    def handle_join_game_response(self, data):
        response_data = form.ServerJoinGame(data)
        log_join = lambda response: ClientInfo.logger.info(f'Game join: {response}')
        if response_data.response_code == form.JoinGameEnum.SUCCESS:
            log_join(form.JoinGameEnum.SUCCESS.name)
            ClientInfo.game_id = response_data.game_id
            # Joiner listens in on Game Queue
            self.game_mq = MessageQueue(queue_name=f'gameserver.{ClientInfo.username}.playing.game.{response_data.game_id}',
                                         exchange=form.game_exchange_name(), routing_key=response_data.game_id)
            self.game_mq.set_consume()
            ClientInfo.logger.info(f'Listening to Game Queue with Queue Name {self.game_mq.queue_name}')
            reactor.callInThread(self.game_mq.start_consumption)
            ClientInfo.join_gui.join_game_success()
            ClientInfo.main_gui.change_screens(form.MenuScreenEnums.WAITING_ROOM)
        elif response_data.response_code == form.JoinGameEnum.WRONG_PASSWORD:
            log_join(form.JoinGameEnum.WRONG_PASSWORD.name)
        elif response_data.response_code == form.JoinGameEnum.JOIN_ITSELF:
            log_join(form.JoinGameEnum.JOIN_ITSELF.name)
        else:
            print('unhandled')
            raise RuntimeError

    @staticmethod
    def handle_ready_game_response(data):
        response_data = form.ServerReadyResponse(data)
        if response_data.response_code == form.ReadyResponseEnum.SUCCESS:
            if response_data.response_type == form.ReadyTypeEnum.READY:
                ClientInfo.playing = True
                ClientInfo.main_gui.ready_success()
            elif response_data.response_type == form.ReadyTypeEnum.UNREADY:
                ClientInfo.playing = False
                ClientInfo.main_gui.ready_success()
        elif response_data.response_code == form.ReadyResponseEnum.ERROR:
            if response_data.response_type == form.ReadyTypeEnum.READY:
                t = False
            elif response_data.response_type == form.ReadyTypeEnum.UNREADY:
                t = True
            else:
                ClientInfo.logger.info('Ready type seems to be unknown')
                raise RuntimeError
            ClientInfo.main_gui.ready_error(t)
        else:
            ClientInfo.logger.info('Unhandled ready error')
            raise RuntimeError

    def handle_bet_response(self, data):
        response_data = form.ServerBetResponse(data)
        match response_data.response_code:
            case form.GeneralEnum.SUCCESS:
                ClientInfo.bet_gui.bet_success()
            case form.GeneralEnum.ERROR:
                ClientInfo.bet_gui.bet_failure()

    @staticmethod
    def handle_cards(self, data):
        response_data = form.ServerGetCards(data)
        if response_data.response_code == form.GeneralEnum.SUCCESS:
            ClientInfo.logger.info('Card request successful')
            ClientInfo.game_gui.set_cards(response_data.cards)
        elif response_data.response_code == form.GeneralEnum.SUCCESS:
            ClientInfo.logger.info('Error with card request')
        else:
            ClientInfo.logger.info('UNKNOWN ERROR')

    def lose_connection(self):
        self.transport.loseConnection()


class ClientCreator(ClientFactory):
    @staticmethod
    def start_connection():
        import colouredlogs
        ClientInfo.logger = logging.getLogger('Main')
        colouredlogs.format('[%(hostname)s] %(asctime)s %(message)s')

        colouredlogs.install(logger=ClientInfo.logger)
        endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
        endpoint.connect(ClientCreator())
        reactor.run()

    @staticmethod
    def stop_reactor():
        print('reactor stopped')
        reactor.stop()
        raise RuntimeError

    def buildProtocol(self, addr):
        ClientInfo.tcpHandler = MainClient()
        return ClientInfo.tcpHandler


class MessageQueue:
    def __init__(self, queue_name, exchange, routing_key=''):
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        my_url = form.message_url()

        self.connection = pika.BlockingConnection(pika.URLParameters(url=my_url))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name, durable=False, exclusive=False, auto_delete=True)
        self.channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)
        ClientInfo.logger.info(f'Message queue object made: queue name: {queue_name}'
                               f' exchange: {exchange} '
                               f'routing key: {routing_key}')

    def start_consumption(self):
        ClientInfo.logger.info('Start consumption')
        self.channel.start_consuming()

    def set_consume(self):
        self.channel.basic_consume(queue=self.queue_name, auto_ack=True, on_message_callback=mq_data_received)

    def stop_consumption(self):
        self.channel.stop_consuming()


def mq_data_received(ch, method, properties, body):
    json_data = body.decode()
    print('THIS DID NOT RUN :)')
    ClientInfo.logger.info(f'{json_data}')
    message = form.ServerRequestHeader(json_data)
    match message.request_type:
        case form.ServerRequestTypeEnum.UPDATE_EVERY_GAME_LIST:
            ClientInfo.main_gui.set_game_list(message.data)
        case form.ServerRequestTypeEnum.UPDATE_PLAYER_LIST:
            ClientInfo.main_gui.set_player_list(message.data)
        case form.ServerRequestTypeEnum.READY_GAME_RESPONSE:
            start_game_response(message.data)
        case form.ServerRequestTypeEnum.STATE_CHANGE:
            state_handler(message.data)


def state_handler(data):
    match data:
        case form.GameState.CARD_CHANGING:
            ClientInfo.tcpHandler.request_cards()


def start_game_response(data):
    sent_data = form.ServerStartResponse(data)
    if sent_data.response_code == form.GeneralEnum.SUCCESS:
        ClientInfo.logger.info('Starting game...')
        if ClientInfo.playing:
            ClientInfo.logger.info('Game started. Loading assets...')
            ClientInfo.main_gui.setup_game()
        else:
            ClientInfo.logger.info('Game started. Not playing')
    elif sent_data.response_code == form.GeneralEnum.ERROR:
        ClientInfo.logger.info('Wrong input data. An error has occured')
    else:
        ClientInfo.logger.info('Unknown error has occurred')
        raise RuntimeError
'''

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.INFO)

    logger = logging.getLogger('Main')
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()

'''