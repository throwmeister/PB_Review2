from enum import Enum
import json


class GameStatus(str, Enum):
    INVALID = 0
    VALID = 1
    STARTING = 2
    IN_PROGRESS = 3


class LoginResponseEnum(str, Enum):
    UNKNOWN_ERROR = 0
    SUCCESS = 1
    ERROR = 2


class ClientRequestTypeEnum(str, Enum):
    UNKNOWN = 0
    KEEP_ALIVE = 404
    LOGIN_REQUEST = 1
    LOGOUT_REQUEST = 2
    CREATE_GAME = 3
    JOIN_GAME = 4


class ServerRequestTypeEnum(str, Enum):
    UNKNOWN = 0
    LOGIN_RESPONSE = 1
    INVALID_SESSION = 2
    CREATE_GAME_RESPONSE = 3
    JOIN_GAME_RESPONSE = 4
    UPDATE_EVERY_GAME_LIST = 5
    UPDATE_ONE_GAME_LIST = 6


class GameTypeEnum(str, Enum):
    UNKNOWN = 0
    POKER = 1
    BLACKJACK = 2


class CreateGameEnum(str, Enum):
    UNKNOWN = 0
    SUCCESS = 1
    NAME_ERROR = 2


class JoinGameEnum(str, Enum):
    UNKNOWN = 0
    SUCCESS = 1
    WRONG_PASSWORD = 2
    NOT_EXIST = 3


class ClientRequestHeader:
    def __init__(self, instructions=None):
        if instructions:
            f = json.loads(instructions)
            self.request_type = f['request_type']
            self.session_id = f['session_id']
            self.data = f['data']
        else:
            self.request_type = ClientRequestTypeEnum.UNKNOWN
            self.session_id = ''
            self.data = None


class ServerRequestHeader:
    def __init__(self, instructions=None):
        if instructions:
            f = json.loads(instructions)
            self.request_type = f['request_type']
            self.data = f['data']
        else:
            self.request_type = ServerRequestTypeEnum.UNKNOWN
            self.data = None


class ClientLoginRequest:
    def __init__(self, data=None):
        if data:
            self.username: str = data['username']
            self.password: str = data['password']
            self.version: str = data['version']
        else:
            self.username = ''
            self.password = ''
            self.version = ''


class ClientLogoutRequest:
    def __init__(self, data=None):
        if data:
            self.username: str = data['username']
        else:
            self.username = ''


class ServerLoginResponse:
    def __init__(self, data=None):
        if data:
            self.username = data['username']
            self.response_code = data['response_code']
            self.message = data['message']
            self.keep_alive = data['keep_alive']
            self.session_id = data['session_id']
        else:
            self.username = ''
            self.response_code = LoginResponseEnum.UNKNOWN_ERROR
            self.message = ''
            self.keep_alive = ''
            self.session_id = ''


class ClientCreateGame:
    def __init__(self, data=None):
        if data:
            self.game_name = data['game_name']
            self.password = data['password']
            self.game_type = data['game_type']
        else:
            self.game_name = ''
            self.password = ''
            self.game_type = GameTypeEnum.UNKNOWN


class ServerCreateGame:
    def __init__(self, data=None):
        if data:
            self.response_code = data['response_code']
            self.game_id = data['game_id']
        else:
            self.response_code = CreateGameEnum.UNKNOWN
            self.game_id = ''


class ClientJoinGame:
    def __init__(self, data=None):
        if data:
            self.game_id = data['game_id']
            self.password = data['password']
        else:
            self.game_id = ''
            self.password = ''


class ServerJoinGame:
    def __init__(self, data=None):
        if data:
            self.response_type = data['response_type']
            self.game_name = data['game_name']
        else:
            self.response_type = JoinGameEnum.UNKNOWN
            self.game_name = ''


class UpdateGameList:
    def __init__(self, data=None):
        if data:
            self.game_id = data['game_id']
            self.game_vars = UpdateGameListVariables(data['game_vars'])
        else:
            pass


class UpdateGameListVariables:
    def __init__(self, data=None):
        if data:
            self.game_name = data['game_name']
            self.game_type = data['game_type']
            self.num_players = data['num_players']
            self.in_progress = data['in_progress']


def version_number():
    return '1.0'


def decode_format():
    return 'utf-8'


def message_url():
    return 'amqps://nueyygmi:rB5rQ_Q7VVq-X8S1ytyilh20EPhcj0S9@rattlesnake.rmq.cloudamqp.com/nueyygmi'


def exchange_name():
    return 'gameserver.broadcast'