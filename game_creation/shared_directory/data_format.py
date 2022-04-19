from enum import Enum, IntEnum
import json


class GameStatus(str, Enum):
    INVALID = 0
    VALID = 1
    STARTING = 2
    IN_PROGRESS = 3


class GeneralEnum(str, Enum):
    UNKNOWN_ERROR = 0
    SUCCESS = 1
    ERROR = 2


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
    READY_GAME = 5
    LEAVE_GAME = 6
    START_GAME = 7
    SEND_BET = 8
    REQUEST_CARDS = 9


class ServerRequestTypeEnum(str, Enum):
    UNKNOWN = 0
    LOGIN_RESPONSE = 1
    INVALID_SESSION = 2
    CREATE_GAME_RESPONSE = 3
    JOIN_GAME_RESPONSE = 4
    UPDATE_EVERY_GAME_LIST = 5
    UPDATE_PLAYER_LIST = 6
    READY_GAME_RESPONSE = 7
    START_GAME_RESPONSE = 8
    BET_RESPONSE = 9
    STATE_CHANGE = 10
    CARDS = 11


class GameTypeEnum(str, Enum):
    UNKNOWN = 0
    POKER = 1
    BLACKJACK = 2


class CreateGameEnum(str, Enum):
    UNKNOWN = 0
    SUCCESS = 1
    NAME_ERROR = 2
    ALREADY_CREATED_GAME = 3


class JoinGameEnum(str, Enum):
    UNKNOWN = 0
    SUCCESS = 1
    WRONG_PASSWORD = 2
    NOT_EXIST = 3
    JOIN_ITSELF = 4


class PlayerReadyEnum(str, Enum):
    FALSE = 0
    TRUE = 1


class ReadyTypeEnum(str, Enum):
    UNKNOWN = 0
    READY = 1
    UNREADY = 2


class ReadyResponseEnum(str, Enum):
    UNKNOWN_ERROR = 0
    SUCCESS = 1
    ERROR = 2


class GameState(str, Enum):
    SETUP = 0
    BETTING = 1
    CARD_CHANGING = 2
    CALCULATING = 3
    LOOP = 4


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
            self.response_code = data['response_code']
            self.game_name = data['game_name']
            self.game_id = data['game_id']
        else:
            self.response_code = JoinGameEnum.UNKNOWN
            self.game_name = ''
            self.game_id = ''


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
            self.owner = data['owner']
        else:
            self.game_name = ''
            self.game_type = GameTypeEnum.UNKNOWN
            self.owner = ''
            self.num_players = 0
            self.in_progress = False


class UpdatePlayerList:
    def __init__(self, data=None):
        if data:
            self.player_name = data['player_name']
            self.ready = data['ready']
        else:
            self.player_name = ''
            self.ready = PlayerReadyEnum.FALSE


class ClientReadyGame:
    def __init__(self, data=None):
        if data:
            self.game_id = data['game_id']
            self.request = data['request']
        else:
            self.game_id = ''
            self.request = ReadyTypeEnum.UNKNOWN


class ServerReadyResponse:
    def __init__(self, data=None):
        if data:
            self.response_code = data['response_code']
            self.response_type = data['response_type']
        else:
            self.response_code = ReadyResponseEnum.UNKNOWN_ERROR
            self.response_type = ReadyTypeEnum.UNKNOWN


class ClientStartGame:
    def __init__(self, data=None):
        if data:
            self.game_id = data['game_id']
        else:
            self.game_id = ''


class ServerStartResponse:
    def __init__(self, data=None):
        if data:
            self.response_code = data['response_code']
            self.game_type = data['game_type']
        else:
            self.response_code = GeneralEnum.UNKNOWN_ERROR
            self.game_type = GameTypeEnum.UNKNOWN


class ClientSendBet:
    def __init__(self, data=None):
        if data:
            self.game_id = data['game_id']
            self.bet = data['bet']
        else:
            self.game_id = ''
            self.bet = 0


class ServerBetResponse:
    def __init__(self, data=None):
        if data:
            self.response_code = data['response_code']
        else:
            self.response_code = GeneralEnum.UNKNOWN_ERROR


class ServerGetCards:
    def __init__(self, data=None):
        if data:
            self.response_code = data['response_code']
            self.cards = data['cards']
        else:
            self.response_code = GeneralEnum.UNKNOWN_ERROR
            self.cards = None


class ExtractCard:
    def __init__(self, data=None):
        if data:
            self.value = data['value']
            self.suit = data['suit']
        else:
            self.value = 0
            self.suit = ''


def version_number():
    return '1.0'


def decode_format():
    return 'utf-8'


def message_url():
    return 'amqps://nueyygmi:rB5rQ_Q7VVq-X8S1ytyilh20EPhcj0S9@rattlesnake.rmq.cloudamqp.com/nueyygmi'


def exchange_name():
    return 'gameserver.broadcast'


def game_exchange_name():
    return 'gameserver.games'


class MenuScreenEnums(IntEnum):
    START = 0
    GAME_LIST = 1
    WAITING_ROOM = 2
