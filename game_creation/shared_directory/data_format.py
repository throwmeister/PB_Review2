from enum import Enum
import json



class LoginResponseEnum(Enum):
    ERROR = 0
    SUCCESS = 1


class HeaderEnum(Enum):
    UNKNOWN = 0
    LOGIN_REQUEST = 1
    LOGIN_RESPONSE = 2


class RequestType:
    def __init__(self, instructions):
        f = json.load(instructions)
        self.request_type = f['request_type']
        self.data = f['data']


class ClientLoginRequest:
    def __init__(self, data: dict):
        self.username = data['username']
        self.password = data['password']
        self.version = data['version']


class ServerLoginResponse:
    def __init__(self, data: dict):
        self.username = data['username']
        self.response_code = data['response_code']
        self.message = data['message']
        self.keep_alive = data['keep_alive']
        self.session_id = data['session_id']
