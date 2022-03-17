import builtins
import session
import shared_directory.data_format as form
from gamerserver_data import DBManager
from configuration_protocol import ServerConfig
import json


def handle_login_requests(data):
    login_data = form.ClientLoginRequest(data)
    # We assume that Usernames cannot be the same
    user_info = DBManager().get_user(login_data.username)
    response_data = form.ServerLoginResponse()
    response_data.username = login_data.username
    response_data.keep_alive = ServerConfig.keep_alive()
    # sent_password = hash(login_data.password) for when we hash passwords
    if login_data.version == form.version_number():
        try:
            username_db, password_db = zip(*user_info)
            username_db, password_db = *username_db, *password_db
        except builtins.ValueError:
            username_db, password_db = None, None
        if login_data.username == username_db and login_data.password == password_db:
            # Create session
            new_session = session.create_session(login_data.username)
            if new_session:
                response_data.response_code = form.LoginResponseEnum.SUCCESS
                response_data.message = 'Your login has been successful'
                response_data.session_id = str(new_session.ID)
            else:
                response_data.message = 'User session already exists and is valid'
                response_data.response_code = form.LoginResponseEnum.ERROR
        else:
            # Return error message to user: wrong username/password
            response_data.message = 'Invalid username/password'
            response_data.response_code = form.LoginResponseEnum.ERROR
    else:
        # Return error to client - need to update software
        response_data.message = 'Invalid client version. Please update your software'
        response_data.response_code = form.LoginResponseEnum.ERROR
    req = form.ServerRequestHeader()
    req.request_type = form.ServerRequestTypeEnum.LOGIN_RESPONSE
    req.data = response_data.__dict__
    return json.dumps(req.__dict__)


def handle_logout(session_id):
    session.Session.delete_session(session_id)


def invalid_session():
    req = form.ServerRequestHeader()
    req.request_type = form.ServerRequestTypeEnum.INVALID_SESSION
    return json.dumps(req.__dict__)
