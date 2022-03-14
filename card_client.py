import time

from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.protocols.basic import LineReceiver
import asyncio


class Client(LineReceiver):
    FORMAT = 'utf-8'

    def __init__(self):
        self.defer = defer.Deferred()

    def connectionMade(self):
        self.transport.write(f'Client {self} has connected\n'.encode(self.FORMAT))

    def lineReceived(self, line):
        print(line.decode(self.FORMAT))
        '''

        def user_input(_):
            user_i = input().encode(self.FORMAT)
            return user_i

        self.defer.addCallback(user_input)
        self.defer.addCallback(self.sendLine)
        self.defer.callback(None)
        '''
        x = self.send_data()
        x.addCallback(self.sendLine)
        print('doing some stuff')
        time.sleep(3)
        print('doing some more stuff')

    def send_data(self):
        d = defer.Deferred()
        d.callback(input().encode(self.FORMAT))
        return d

        # self.defer.addCallback(self.sendLine)
        # self.defer.addCallback(self.transport.write)
        print('it has reached this')


'''
    def dataReceived(self, data: bytes):
        print(data.decode(self.FORMAT))
'''


class ClientF(ClientFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientF())
    reactor.run()
