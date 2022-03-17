from twisted.internet import reactor, endpoints
from twisted.internet.protocol import ServerFactory, Protocol
# from configuration_protocol import ServerConfig
import shared_directory.data_format as form
import s_message_handler as handler
import session


class MainServer(Protocol):
    format = form.decode_format()

    def connectionMade(self):
        pass

    def dataReceived(self, data: bytes):
        sp_data = data.decode(self.format).split('\r')
        print(sp_data)
        for d in sp_data:
            print(d)
            messages = form.ClientRequestHeader(d)
            if messages.request_type == form.ClientRequestTypeEnum.LOGIN_REQUEST:
                data = handler.handle_login_requests(messages.data)
                self.transport.write(f'{data}\r'.encode(self.format))
            # Validate session updates the activity timer. Therefore, no need to call it for the keep alive
            elif session.Session.validate_session(messages.session_id):
                match messages.request_type:
                    case form.ClientRequestTypeEnum.KEEP_ALIVE:
                        print(f'keep alive message received from {messages.session_id}: {messages.data}')
                    case form.ClientRequestTypeEnum.LOGOUT_REQUEST:
                        handler.handle_logout(messages.session_id)
                        print('logout successful')
            else:
                print('Invalid session request')
                data = handler.invalid_session()
                self.transport.write(f"{data}\r".encode(self.format))


class ServerProtocol(ServerFactory):
    def buildProtocol(self, addr):
        return MainServer()


if __name__ == '__main__':
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(ServerProtocol())
    reactor.run()
