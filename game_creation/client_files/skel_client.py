import time

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
from game_creation.shared_directory import data_format as form
from client_data import ClientInfo
import c_message_handler as handler
import json


# noinspection PyArgumentList
class MainClient(Protocol):
    format = form.decode_format()

    def __init__(self):
        self.client_info: ClientInfo = ClientInfo()

    def connectionMade(self):
        # Do we want the client to be auto logged in?
        # Do we want to save the login details if they have logged in before?
        self.send_login()

    def connectionLost(self, reason):
        print('disconnecting')
        # self.send_logout()

    def send_login(self):
        x = form.ClientLoginRequest()
        x.username = 'Alex'
        x.password = 'alex'
        x.version = form.version_number()
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        print('send login')
        self.transport.write(f'{s}\r'.encode(self.format))

    def send_logout(self):
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGOUT_REQUEST
        req.session_id = self.client_info.session_id
        req.data = ''
        s = json.dumps(req.__dict__)
        self.transport.write(f'{s}\r'.encode(self.format))
        print('sent logout')

    def dataReceived(self, data: bytes):
        sp_data = data.decode(self.format).split('\r')
        for d in sp_data:
            print(d)
            message = form.ServerRequestHeader(d)
            match message.request_type:
                case form.ServerRequestTypeEnum.LOGIN_RESPONSE:
                    print('login response')
                    self.handle_login_response(message.data)
                case form.ServerRequestTypeEnum.INVALID_SESSION:
                    # Stop keep alive function
                    pass
                case _:
                    # Invalid command
                    pass

    def handle_login_response(self, data):
        response_data = form.ServerLoginResponse(data)
        print(response_data.message)
        if response_data.response_code == form.LoginResponseEnum.SUCCESS:
            self.client_info = ClientInfo(response_data.username, response_data.keep_alive, response_data.session_id)
            # reactor.callInThread()

            reactor.callFromThread(self.start_keep_alive, response_data.keep_alive)
            self.send_logout()
        elif response_data.response_code == form.LoginResponseEnum.ERROR:
            # User must re-input
            # self.send_login()
            pass
        else:
            raise RuntimeError

    def start_keep_alive(self, keep_alive):
        def send_keep_alive():
            response_data = form.ClientRequestHeader()
            response_data.request_type = form.ClientRequestTypeEnum.KEEP_ALIVE
            response_data.session_id = self.client_info.session_id
            response_data.data = self.client_info.username
            s = json.dumps(response_data.__dict__)
            self.transport.write(f'{s}\r'.encode(self.format))

        g = LoopingCall(send_keep_alive)
        g.start(keep_alive)


class ClientCreator(ClientFactory):
    def buildProtocol(self, addr):
        return MainClient()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()
