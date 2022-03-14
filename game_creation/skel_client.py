from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
import json

class MainClient(Protocol):

    def connectionMade(self):
        pass


class ClientCreator(ClientFactory):

    def buildProtocol(self, addr):
        return MainClient()

if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()
