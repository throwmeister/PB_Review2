from twisted.internet import reactor, endpoints
from twisted.internet.protocol import ServerFactory, Protocol
from session import Session
import json
from configuration_protocol import ServerConfig
import shared_directory.data_format as form
import message_handler as handler



class MainServer(Protocol):
    format = ServerConfig.decode_format()

    def connectionMade(self):
        pass

    def dataReceived(self, data: bytes):
        d = data.decode(self.format)
        header = form.RequestType(d)
        match header.request_type:
            case form.HeaderEnum.LOGIN_REQUEST:
                handler.handle_login_requests(header.data)
            case _:
                pass


    def create_session(self, name):
        Session(name)


class ServerProtocol(ServerFactory):
    def buildProtocol(self, addr):
        return MainServer()


if __name__ == '__main__':
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(ServerProtocol())
    reactor.run()

