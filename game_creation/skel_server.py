import builtins

from twisted.internet import reactor, endpoints
from twisted.internet.protocol import ServerFactory, Protocol
# from configuration_protocol import ServerConfig
import shared_directory.data_format as form
import s_message_handler as handler
import session
import json

import pika
import pika.adapters.twisted_connection as tw
import pika.channel as chan

# noinspection PyArgumentList
class MainServer(Protocol):
    format = form.decode_format()

    def connectionMade(self):
        pass

    def login(self, data):
        self.format_send_data(form.ServerRequestTypeEnum.LOGIN_RESPONSE, data)

    def invalid_session(self):
        self.format_send_data(form.ServerRequestTypeEnum.INVALID_SESSION)

    def send_create_game(self, data):
        self.format_send_data(form.ServerRequestTypeEnum.CREATE_GAME_RESPONSE, data)

    def send_join_game(self, data):
        self.format_send_data(form.ServerRequestTypeEnum.JOIN_GAME_RESPONSE, data)

    def format_send_data(self, request_type, data=None):
        req = form.ServerRequestHeader()
        req.request_type = request_type
        if data:
            try:
                req.data = data.__dict__
            except builtins.AttributeError:
                req.data = data
        else:
            req.data = ''
        print(request_type.name)
        s = json.dumps(req.__dict__)
        self.transport.write(f'{s}\r'.encode(self.format))

    def dataReceived(self, data: bytes):
        sp_data = data.decode(self.format).split('\r')
        remove = [x for x in sp_data if x]
        for d in remove:
            print(d)
            messages = form.ClientRequestHeader(d)
            if messages.request_type == form.ClientRequestTypeEnum.LOGIN_REQUEST:
                server_data = handler.handle_login_requests(messages.data)
                self.login(server_data)
            # Validate session updates the activity timer. Therefore, no need to call it for the keep alive
            elif session.Session.validate_session(messages.session_id):
                match messages.request_type:
                    case form.ClientRequestTypeEnum.KEEP_ALIVE:
                        print(f'keep alive message received from {messages.session_id}: {messages.data}')
                    case form.ClientRequestTypeEnum.LOGOUT_REQUEST:
                        session.Session.delete_session(messages.session_id)
                        print('logout successful')
                    case form.ClientRequestTypeEnum.CREATE_GAME:
                        server_data = handler.handle_create_game(messages.data, messages.session_id)
                        self.send_create_game(server_data)
                    case form.ClientRequestTypeEnum.JOIN_GAME:
                        server_data = handler.handle_join_game(messages.data, messages.session_id)
                        self.send_join_game(server_data)
                    case _:
                        pass

            else:
                print('Invalid session request')
                self.invalid_session()


class ServerProtocol(ServerFactory):
    def buildProtocol(self, addr):
        return MainServer()


class MessageQueue:
    def __init__(self, queue_name, exchange, routing_key=''):
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        my_url = form.message_url()

        self.connection = pika.BlockingConnection(pika.URLParameters(url=my_url))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name, durable=True, exclusive=False, auto_delete=False)

    def send_message(self, message):
        self.channel.basic_publish(self.exchange, body=message, routing_key=self.routing_key)

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(ServerProtocol())
    reactor.run()

