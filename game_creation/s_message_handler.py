import shared_directory.data_format as form
from gamerserver_data import DBManager
from configuration_protocol import ServerConfig
import json


def handle_login_requests(data):
    login_data = form.ClientLoginRequest(data)
    # We assume that Usernames cannot be the same
    user_info = DBManager().get_user(login_data.username)

    username_db, password_db = zip(*user_info)
    username_db, password_db = *username_db, *password_db

    response_data = form.ServerLoginResponse()
    response_data.username = login_data.username
    response_data.keep_alive = ServerConfig.keep_alive()
    # sent_password = hash(login_data.password) for when we hash passwords
    if login_data.version == form.version_number():
        if login_data.username == username_db and login_data.password == password_db:
            from session import create_session
            # Create session
            session = create_session(login_data.username)
            if session:
                response_data.response_code = form.LoginResponseEnum.SUCCESS
                response_data.message = 'Your login has been successful'
                response_data.session_id = str(session.ID)
            else:
                response_data.message = 'User session already exists and is valid'
        else:
            # Return error message to user: wrong username/password
            response_data.message = 'Invalid username/password'
    else:
        # Return error to client - need to update software
        response_data.message = 'Invalid client version. Please update your software'
    req = form.ServerRequestHeader()
    req.request_type = form.ServerRequestTypeEnum.LOGIN_RESPONSE
    req.data = response_data.__dict__
    return json.dumps(req.__dict__)
