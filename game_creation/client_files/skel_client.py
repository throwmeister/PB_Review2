import builtins, logging, json, pika

from twisted.internet.defer import Deferred
from twisted.internet.threads import deferToThread
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
from game_creation.shared_directory import data_format as form
from client_data import ClientInfo


# noinspection PyArgumentList
class MainClient(Protocol):
    format = form.decode_format()

    def __init__(self):
        self.client_info: ClientInfo = ClientInfo()
        self.loop: LoopingCall = LoopingCall(self.send_keep_alive)

    def connectionMade(self):
        # Do we want the client to be auto logged in?
        # Do we want to save the login details if they have logged in before?
        self.send_login()

    def connectionLost(self, reason):
        print('disconnecting')

    def send_login(self):
        x = form.ClientLoginRequest()
        x.username = 'Alex'
        x.password = 'alex'
        x.version = form.version_number()
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        logger.info('Send login')
        self.transport.write(f'{s}\r'.encode(self.format))

    def send_logout(self):
        logger.info('Send logout')
        self.format_send_data(form.ClientRequestTypeEnum.LOGOUT_REQUEST)

    def create_game(self, name=None, password=None):
        user_data = form.ClientCreateGame()
        user_data.game_type = form.GameTypeEnum.POKER
        user_data.game_name = 'Alex has a lobby'
        user_data.password = 'ILOVEPOKER'
        self.format_send_data(form.ClientRequestTypeEnum.CREATE_GAME, user_data)

    def join_game(self, game_id, password=None):
        user_data = form.ClientJoinGame()
        user_data.game_id = game_id
        user_data.password = 'ILOVEPOKER'
        self.format_send_data(form.ClientRequestTypeEnum.JOIN_GAME, user_data)

    def format_send_data(self, request_type: form.ClientRequestTypeEnum, data=None):
        req = form.ClientRequestHeader()
        req.request_type = request_type
        req.session_id = self.client_info.session_id
        if data:
            try:
                req.data = data.__dict__
            except builtins.AttributeError:
                req.data = data
        else:
            req.data = ''
        s = json.dumps(req.__dict__)
        logger.debug(f'{request_type.name}')
        self.transport.write(f'{s}\r'.encode(self.format))

    def dataReceived(self, data: bytes):
        sp_data = data.decode(self.format).split('\r')
        remove = [x for x in sp_data if x]
        for d in remove:
            logger.debug(f'{d}')
            message = form.ServerRequestHeader(d)
            match message.request_type:
                case form.ServerRequestTypeEnum.LOGIN_RESPONSE:
                    logger.info('Handling login')
                    self.handle_login_response(message.data)
                case form.ServerRequestTypeEnum.INVALID_SESSION:
                    # Stop keep alive function
                    logger.error('Invalid session. Log in')
                    self.loop.stop()
                case form.ServerRequestTypeEnum.CREATE_GAME_RESPONSE:
                    self.handle_create_game_response(message.data)
                case form.ServerRequestTypeEnum.JOIN_GAME_RESPONSE:
                    self.handle_join_game_response
                case _:
                    # Invalid command
                    pass

    def handle_login_response(self, data):
        response_data = form.ServerLoginResponse(data)
        logger.debug(response_data.message)
        if response_data.response_code == form.LoginResponseEnum.SUCCESS:
            self.client_info = ClientInfo(response_data.username, response_data.keep_alive, response_data.session_id)
            self.loop.start(response_data.keep_alive)
            # reactor.callFromThread(self.start_keep_alive, response_data.keep_alive)
            self.create_game()
        elif response_data.response_code == form.LoginResponseEnum.ERROR:
            # User must re-input
            # self.send_login()
            pass
        else:
            raise RuntimeError

    def send_keep_alive(self):
        self.format_send_data(form.ClientRequestTypeEnum.KEEP_ALIVE, self.client_info.username)

    def handle_create_game_response(self, data):
        response_data = form.ServerCreateGame(data)
        if response_data.response_code == form.CreateGameEnum.SUCCESS:
            logger.info(f'Game creation: {form.CreateGameEnum.SUCCESS.name}')
            self.client_info.game_joined = response_data.game_id
            self.client_info.game_owner = True
        elif response_data.response_code == form.CreateGameEnum.NAME_ERROR:
            # Popup
            logger.info(f'Game creation: {form.CreateGameEnum.NAME_ERROR.name}')
        else:
            raise RuntimeError

    def handle_join_game_response(self, data):
        pass


class ClientCreator(ClientFactory):
    def buildProtocol(self, addr):
        return MainClient()


class MessageQueue:
    def __init__(self, queue_name, exchange, routing_key=''):
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        my_url = form.message_url()

        self.connection = pika.BlockingConnection(pika.URLParameters(url=my_url))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name, durable=True, exclusive=False, auto_delete=False)
        self.channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)

        def callback(ch, method, properties, body):
            print(f'Received: {body.decode()}')
            print(f'''ch: {ch}
        method: {method}
        properties: {properties}
        ''')

        def called():
            pass

        self.channel.basic_consume(queue=queue_name,
                              on_message_callback=self.dataRecieved)

        self.channel.start_consuming()

    def dataRecieved(self, ch, method, properties, body):
        print(f'Received: {body.decode()}')
        print(f'''ch: {ch}
                method: {method}
                properties: {properties}
                ''')



if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG)

    logger = logging.getLogger('Main')
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()
    print('run...')
    x = MessageQueue(queue_name='gaming.client.lobby', exchange='gameserver.broadcast')
