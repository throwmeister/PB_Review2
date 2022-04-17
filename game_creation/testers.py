import json
import enum
import shared_directory.data_format as form

x = hash('3')
print(x)

t = {"password": "john"}
f = t['password']
print(hash(f))
g = json.dumps(t)
print(g)
e = json.loads(g)
print(e)


class ServerLoginResponse:

    def __init__(self, data=None):
        self.name = 'alex'

x = ServerLoginResponse()
print(x.__dict__)

x = {'username': 'alex'}
print(x.values())
for s in x.values():
    print(s)


class Test(str, enum.Enum):
    A = 0
    B = 1


print(Test.A.name)

if '':
    print('not working')
else:
    print('working')

if t['password']:
    print('testing')

try:
    var = x['penis']
except KeyError:
    print('no way')

values = {'h': 'hello', 'p': 'pussio'}
for k, v in values.items():
    print(f'{k}, {v}')

n, m = [1, 2]
print(n)
print(m)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display(self):
        print(f'{self.value} of {self.suit}')

    def return_card(self):
        return f'{self.value} of {self.suit}'

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def __str__(self):
        return f'{self.value} of {self.suit}'

card = Card('spades', 7)
print(card.__dict__)
