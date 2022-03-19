from twisted.internet.protocol import Protocol, ServerFactory, Factory
from twisted.internet import endpoints, reactor
from twisted.protocols import basic
from old_files.games_logic import Poker, PokerPlayer, Blackjack, BlackjackPlayer


class Echo(basic.LineReceiver):
    FORMAT = 'utf-8'

    def __init__(self, game):
        self.game = game
        self.state = 'ENTERNAME'

    def connectionMade(self):
        self.transport.write('Welcome to poker\n'.encode(self.FORMAT))
        self.sendLine(b'What is your name?')

    def lineReceived(self, line):
        print(f'Line {line.decode(self.FORMAT)} received')
        self.transport.write(b'Received data')
        match self.state:
            case 'ENTERNAME':
                self.game.add_player(line, 100)
                print('added player')
            case _:
                pass


class PBFactory(ServerFactory):
    def __init__(self, gtype):
        self.instance = gtype

    def buildProtocol(self, addr):
        return Echo(self.instance)


if __name__ == '__main__':
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
    gameclass = Poker(PokerPlayer)
    endpoint.listen(PBFactory(gameclass))
    reactor.run()
