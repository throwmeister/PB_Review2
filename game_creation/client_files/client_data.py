
class ClientInfo:
    username = ''
    keep_alive = 0
    session_id = ''
    game_joined = ''
    game_owner = False
    valid_session = False

    tcpHandler = None
    main_gui = None
    login_gui = None
    create_game_gui = None
    join_gui = None
    logger = None

    @classmethod
    def set_login_values(cls, username, keepalive, session_id):
        cls.username = username
        cls.keep_alive = keepalive
        cls.session_id = session_id


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

