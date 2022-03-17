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
        self.send_login('Alex', 'alex')

    def send_login(self, username, password):
        x = form.ClientLoginRequest()
        x.username = username
        x.password = password
        x.version = form.version_number()
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        self.transport.write(s.encode(self.format))

    def dataReceived(self, data: bytes):
        d = data.decode(self.format)
        print(d)
        message = form.ServerRequestHeader(d)
        match message.request_type:
            case form.ServerRequestTypeEnum.LOGIN_RESPONSE:
                print('login response')
                self.handle_login_response(message.data)
            case _:
                # Invalid command
                pass

    def handle_login_response(self, data):
        response_data = form.ServerLoginResponse(data)
        print(response_data.message)
        if response_data.response_code == form.LoginResponseEnum.SUCCESS:
            self.client_info = ClientInfo(response_data.username, response_data.keep_alive, response_data.session_id)
            # reactor.callInThread()

            def threader():
                g = LoopingCall(self.send_keep_alive)
                g.start(20)

            reactor.callInThread(threader)
            reactor.callInThread(self.testing)
        elif response_data.response_code == form.LoginResponseEnum.ERROR:
            # User must re-input
            pass
        else:
            raise RuntimeError

    def testing(self):
        input()
        print('g')

    def send_keep_alive(self):
        response_data = form.ClientRequestHeader()
        response_data.request_type = form.ClientRequestTypeEnum.KEEP_ALIVE
        response_data.session_id = self.client_info.session_id



class ClientCreator(ClientFactory):
    def buildProtocol(self, addr):
        return MainClient()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()
