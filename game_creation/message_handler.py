import shared_directory.data_format as form
from configuration_protocol import ServerConfig
from gamerserver_data import DBManager


def handle_login_requests(data):
    login_data = form.ClientLoginRequest(data)
    # We assume that Usernames cannot be the same
    user_info = DBManager().get_user(login_data.username)

    username_db, password_db = zip(*user_info)
    username_db, password_db = *username_db, *password_db

    # sent_password = hash(login_data.password) for when we hash passwords
    if login_data.version == ServerConfig.version_number():
        if login_data.username == username_db and login_data.password == password_db:
            # Create session
            pass
        else:
            # Return error message to user: wrong username/password
            pass
    else:
        # Return error to client - need to update software
        pass


def send_login_response():
    pass