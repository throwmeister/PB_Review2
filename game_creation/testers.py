import json

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
