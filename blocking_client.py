from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
import asyncio


class Client(Protocol):
    FORMAT = 'utf-8'

    def __init__(self):
        self.defer = defer.Deferred()

    def connectionMade(self):
        self.transport.write('Client has connected\n'.encode(self.FORMAT))
        for _ in range(30):
            self.transport.write('IM BLOCKING HAHAHAHAHA\n'.encode(self.FORMAT))


    def dataReceived(self, data: bytes):
        print(data.decode(self.FORMAT))


class ClientF(ClientFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientF())
    reactor.run()
