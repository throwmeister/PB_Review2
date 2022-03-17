from twisted.internet import reactor, endpoints
from twisted.internet.protocol import ServerFactory, Protocol
from configuration_protocol import ServerConfig
import shared_directory.data_format as form
import s_message_handler as handler
import session


class MainServer(Protocol):
    format = form.decode_format()

    def connectionMade(self):
        pass

    def dataReceived(self, data: bytes):
        d = data.decode(self.format)
        messages = form.ClientRequestHeader(d)
        if messages.request_type == form.ClientRequestTypeEnum.LOGIN_REQUEST:
            data = handler.handle_login_requests(messages.data)
            self.transport.write(data.encode(self.format))
        elif session.Session.validate_session(messages.session_id):
            match messages.request_type:
                case _:
                    pass
        else:
            print('Invalid session')


class ServerProtocol(ServerFactory):
    def buildProtocol(self, addr):
        return MainServer()


if __name__ == '__main__':
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(ServerProtocol())
    reactor.run()

