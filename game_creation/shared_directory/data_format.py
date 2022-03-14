from enum import Enum
import json


class LoginResponseEnum(str, Enum):
    ERROR = 0
    SUCCESS = 1


class RequestTypeEnum(str, Enum):
    UNKNOWN = 0
    LOGIN_REQUEST = 1
    LOGIN_RESPONSE = 2


class RequestType:
    def __init__(self, instructions=None):
        if instructions:
            f = json.loads(instructions)
            self.request_type = f['request_type']
            self.data = f['data']
        else:
            self.request_type = RequestTypeEnum.UNKNOWN
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
            self.response_code = LoginResponseEnum.ERROR
            self.message = ''
            self.keep_alive = ''
            self.session_id = ''


def version_number():
    return '1.0'


def decode_format():
    return 'utf-8'