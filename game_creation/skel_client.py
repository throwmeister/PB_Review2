from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
import shared_directory.data_format as form
import json


class MainClient(Protocol):
    format = form.decode_format()

    def connectionMade(self):
        self.send_login()

    def send_login(self):
        x = form.ClientLoginRequest()
        x.username = 'Alex'
        x.password = 'alexhvggujhv'
        x.version = form.version_number()
        req = form.RequestType()
        req.request_type = form.RequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        self.transport.write(s.encode(self.format))

    def dataReceived(self, data: bytes):
        d = data.decode(self.format)
        print(d)

class ClientCreator(ClientFactory):

    def buildProtocol(self, addr):
        return MainClient()

if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()
