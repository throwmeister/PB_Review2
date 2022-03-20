class ClientInfo:
    def __init__(self, username=None, keepalive=None, session_id=None):
        self.username = username
        self.keepalive = keepalive
        self.session_id = session_id
        self.game_joined = ''
        self.game_owner = False


class GameLobbies:
    Games = {}

    def __init__(self, name, game_id, game_type):
        self.name = name
        self.game_id = game_id
        self.game_type = game_type
        self.num_players = int
        self.Games[game_id] = self

    def update_num(self, num):
        self.num_players = num

