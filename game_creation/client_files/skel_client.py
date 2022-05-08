import builtins, logging, json, pika
'''
from twisted.internet.defer import Deferred
from twisted.internet.threads import deferToThread
'''

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
import game_creation.shared_directory.data_format as form
from client_data import ClientInfo, GameInfo

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

    def request_start_signal(self):
        self.format_send_data(form.ClientRequestTypeEnum.SIGNAL_START)

    def send_bet(self, amount, all_in):
        user_data = form.ClientSendBet()
        user_data.bet = amount
        user_data.game_id = ClientInfo.game_id
        user_data.all_in = form.AllInEnum.NO
        if all_in:
            user_data.all_in = form.AllInEnum.YES
        if GameInfo.state == form.GameState.BETTING:
            self.format_send_data(form.ClientRequestTypeEnum.SEND_BET, user_data)
        elif GameInfo.state == form.GameState.BETTING_TWO:
            self.format_send_data(form.ClientRequestTypeEnum.SEND_BET_TWO, user_data)

    def request_cards(self):
        self.format_send_data(form.ClientRequestTypeEnum.REQUEST_CARDS, ClientInfo.game_id)

    def send_replace_cards(self, cards):
        user_data = form.ClientSendCards()
        user_data.game_id = ClientInfo.game_id
        user_data.cards = cards
        self.format_send_data(form.ClientRequestTypeEnum.POKER_SEND_CARDS, user_data)

    def send_fold(self):
        user_data = form.ClientFold()
        user_data.game_id = ClientInfo.game_id
        self.format_send_data(form.ClientRequestTypeEnum.FOLD, user_data)

    def send_leave_game(self):
        self.format_send_data(form.ClientRequestTypeEnum.LEAVE_GAME, ClientInfo.game_id)

    def send_hit(self):
        self.format_send_data(form.ClientRequestTypeEnum.BLACKJACK_HIT, ClientInfo.game_id)

    def send_hold(self):
        self.format_send_data(form.ClientRequestTypeEnum.BLACKJACK_HOLD, ClientInfo.game_id)

    def send_double(self):
        self.format_send_data(form.ClientRequestTypeEnum.DOUBLE, ClientInfo.game_id)

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
                case form.ServerRequestTypeEnum.REPLACED_CARDS:
                    self.handle_replaced_cards(message.data)
                case form.ServerRequestTypeEnum.SIGNAL_START:
                    ClientInfo.main_gui.setup_game()
                case form.ServerRequestTypeEnum.HIT_RESPONSE:
                    self.handle_hit_response(message.data)
                case form.ServerRequestTypeEnum.HOLD_RESPONSE:
                    self.handle_hold_response(message.data)
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
            if self.lobby_mq:
                self.lobby_mq.stop_consumption()
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
            ClientInfo.logger.info('UNKNOWN ERROR')
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
            if self.game_mq:
                self.game_mq.stop_consumption()
            self.game_mq = MessageQueue(queue_name=f'gameserver.{ClientInfo.username}.playing.game.{response_data.game_id}',
                                         exchange=form.game_exchange_name(), routing_key=response_data.game_id)
            self.game_mq.set_consume()
            reactor.callInThread(self.game_mq.start_consumption)
            ClientInfo.logger.info(f'Listening to Game Queue with Queue Name {self.game_mq.queue_name}')
            ClientInfo.create_game_gui.create_response_success()
            ClientInfo.main_gui.change_screens(form.MenuScreenEnums.WAITING_ROOM)
        elif response_data.response_code == form.CreateGameEnum.NAME_ERROR:
            ClientInfo.create_game_gui.create_game_name_exists()
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.NAME_ERROR.name}')
        elif response_data.response_code == form.CreateGameEnum.ALREADY_CREATED_GAME:
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.ALREADY_CREATED_GAME.name}')
        elif response_data.response_code == form.CreateGameEnum.INVALID_CREDENTIALS:
            ClientInfo.create_game_gui.create_game_invalid_credentials()
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.INVALID_CREDENTIALS.name}')
        else:
            raise RuntimeError

    def handle_join_game_response(self, data):
        response_data = form.ServerJoinGame(data)
        log_join = lambda response: ClientInfo.logger.info(f'Game join: {response}')
        if response_data.response_code == form.JoinGameEnum.SUCCESS:
            log_join(form.JoinGameEnum.SUCCESS.name)
            ClientInfo.game_id = response_data.game_id
            # Joiner listens in on Game Queue
            if self.game_mq:
                self.game_mq.stop_consumption()
            ClientInfo.message_queue = MessageQueue(queue_name=f'gameserver.{ClientInfo.username}.playing.game.{response_data.game_id}',
                                         exchange=form.game_exchange_name(), routing_key=response_data.game_id)
            self.game_mq = ClientInfo.message_queue
            self.game_mq.set_consume()
            ClientInfo.logger.info(f'Listening to Game Queue with Queue Name {self.game_mq.queue_name}')
            reactor.callInThread(self.game_mq.start_consumption)
            ClientInfo.join_gui.join_game_success()
            ClientInfo.main_gui.change_screens(form.MenuScreenEnums.WAITING_ROOM)
        elif response_data.response_code == form.JoinGameEnum.WRONG_PASSWORD:
            log_join(form.JoinGameEnum.WRONG_PASSWORD.name)
            ClientInfo.join_gui.join_game_wrong_password()
        elif response_data.response_code == form.JoinGameEnum.JOIN_ITSELF:
            log_join(form.JoinGameEnum.JOIN_ITSELF.name)
        else:
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
                ClientInfo.logger.info('Bet success')
                ClientInfo.main_gui.bet_success()
            case form.GeneralEnum.ERROR:
                ClientInfo.logger.info('Bet failure')
                ClientInfo.bet_gui.bet_failure()

    @staticmethod
    def handle_cards(data):
        response_data = form.ServerGetCards(data)
        if response_data.response_code == form.GeneralEnum.SUCCESS:
            ClientInfo.logger.info('Card request successful')
            ClientInfo.main_gui.set_cards(response_data.cards)
        elif response_data.response_code == form.GeneralEnum.ERROR:
            ClientInfo.logger.info('Error with card request')
        else:
            ClientInfo.logger.info('UNKNOWN ERROR')

    @staticmethod
    def handle_replaced_cards(data):
        response_data = form.ServerGetCards(data)
        if response_data.response_code == form.GeneralEnum.SUCCESS:
            ClientInfo.logger.info('Cards replaced successfully')
            ClientInfo.main_gui.set_cards(response_data.cards)
        elif response_data.response_code == form.GeneralEnum.ERROR:
            ClientInfo.logger.info('Error with card request')

    @staticmethod
    def handle_hit_response(data):
        response_data = form.ServerHitResponse(data)
        if response_data.response_code == form.HitEnum.HIT_SUCCESS:
            ClientInfo.logger.info('Hit - no bust')
            ClientInfo.main_gui.add_card_to_list()
            ClientInfo.main_gui.set_cards(response_data.cards)
            ClientInfo.main_gui.hit_response()
            ClientInfo.main_gui.popup_screen('Hit response', 'Success')
        elif response_data.response_code == form.HitEnum.BUST:
            ClientInfo.logger.info('Hit - bust!')
            ClientInfo.main_gui.add_card_to_list()
            ClientInfo.main_gui.set_cards(response_data.cards)
            ClientInfo.main_gui.player_holding()
            ClientInfo.main_gui.popup_screen('Hit response', 'You have gone bust')
        else:
            ClientInfo.logger.error('Error with hit')
            ClientInfo.main_gui.hit_received()

    @staticmethod
    def handle_hold_response(data):
        data = form.ServerHoldResponse(data)
        match data.response_code:
            case form.GeneralEnum.SUCCESS:
                ClientInfo.main_gui.player_holding()
            case form.GeneralEnum.ERROR:
                ClientInfo.logger.error('An has occurred holding')
                ClientInfo.main_gui.hold_failed()

    def stop_reactor(self):
        self.loop.stop()
        ClientInfo.logger.info('reactor stopped')
        reactor.stop()

    def stop_message_queue(self):
        if self.lobby_mq:
            self.lobby_mq.stop_consumption()
        if self.game_mq:
            self.game_mq.stop_consumption()

    def lose_connection(self):
        self.transport.loseConnection()


class ClientCreator(ClientFactory):
    @staticmethod
    def start_connection():
        import colouredlogs
        ClientInfo.logger = logging.getLogger('Main')
        colouredlogs.format('[%(hostname)s] %(asctime)s %(message)s')

        colouredlogs.install(logger=ClientInfo.logger)
        endpoint = TCP4ClientEndpoint(reactor, form.server_ip(), 8007)
        endpoint.connect(ClientCreator())
        reactor.run()
        quit()

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
    ClientInfo.logger.info('Received from message queue')
    json_data = body.decode()

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
        case form.ServerRequestTypeEnum.GAME_WINNERS:
            winner_calculation_response(message.data)
        case form.ServerRequestTypeEnum.BET_LIST:
            ClientInfo.main_gui.set_bet_list(message.data)
        case form.ServerRequestTypeEnum.BLACKJACK_CARD_PLAYER:
            ClientInfo.main_gui.set_blackjack_table(message.data)


def state_handler(data):
    if ClientInfo.playing:
        match data:
            case form.GameState.CARD_CHANGING:
                ClientInfo.logger.info('Betting section complete')
                GameInfo.state = form.GameState.CARD_CHANGING
                ClientInfo.main_gui.all_bets_done()
                # ClientInfo.tcpHandler.request_cards()
            case form.GameState.BETTING_TWO:
                GameInfo.state = form.GameState.BETTING_TWO
                ClientInfo.logger.info('Betting section 2')
                ClientInfo.main_gui.enable_second_bet()


def start_game_response(data):
    sent_data = form.ServerStartResponse(data)
    if sent_data.response_code == form.GeneralEnum.SUCCESS:
        ClientInfo.logger.info('Starting game...')
        if ClientInfo.playing:
            ClientInfo.logger.info('Game started. Loading assets...')
            ClientInfo.main_gui.setup_game(sent_data.game_type)
        else:
            ClientInfo.logger.info('Game started. Not playing')
    elif sent_data.response_code == form.GeneralEnum.ERROR:
        ClientInfo.logger.info('Wrong input data. An error has occured')
    else:
        ClientInfo.logger.info('Unknown error has occurred')
        raise RuntimeError
    ClientInfo.logger.info('This function has been completed')


def winner_calculation_response(winners):
    if ClientInfo.playing:
        for d in winners:
            player = form.GameWinnerVars(d)
            ClientInfo.logger.info(f'Winner: {player.name}')
            if player.session == ClientInfo.session_id:
                ClientInfo.main_gui.handle_won(player.winnings)
        ClientInfo.main_gui.player_won_popup(winners)
        ClientInfo.main_gui.reset_game_loop()
