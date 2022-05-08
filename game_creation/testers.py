import json
from enum import Enum
import shared_directory.data_format as form
import socket

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


class Test(str, Enum):
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

delist = ['john', 'alex', 'alan']
delist.pop(0)
print(delist)


class GameState(str, Enum):
    SETUP = 0
    BETTING = 1
    CARD_CHANGING = 2
    CALCULATING = 3
    LOOP = 4


req = {'state': GameState.CARD_CHANGING, 'game_id': '3i2194u12385y18'}

s = json.dumps(req)
print(s)

if isinstance('????', Enum):
    print('wheyyy')

for c in []:
    print('teegee')

dictionary = {'suit': 'Spades', 'value': 4}
sped = [{'value': 4, 'suit': 'Spades'}, {'suit': 'Spades', 'value': 7}]

if dictionary in sped:
    sped.remove(dictionary)
    print('yayyyyy')
    print(sped)



test_dict = [[1, 'p'], [3, 'd'], [3, 'f'], [2, 'g']]
print(test_dict)
x =sorted(test_dict, key=lambda x: x[0], reverse=True)
print(x)
f = [g[1] for g in x if g[0] != x[0][0]]
print(f)

if -1:
    print('hehehehehweduiqwfiwnbvjhsfnvsdnvjsncvoasnvjsvbo njf')

print(socket.gethostbyname(socket.gethostname()))
print(hash('alex'))
print(hash('grant'))

import hashlib

print(hashlib.sha1(b'great_password').hexdigest())

f = [g for g in x if g[0] == x[0][0]]
print(f)

print(self.great)