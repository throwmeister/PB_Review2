import builtins
import session
from games_data import Game, Participant
import shared_directory.data_format as form
from gamerserver_data import DBManager
from configuration_protocol import ServerConfig
import json, logging


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
                print('It already exists')
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
    return response_data.__dict__


def handle_logout(session_id):
    session.Session.delete_session(session_id)


def handle_create_game(data, session_id):
    client_data = form.ClientCreateGame(data)
    send_data = form.ServerCreateGame()
    if Game.lobby_name_exists(client_data.game_name):
        # raise error
        send_data.response_code = form.CreateGameEnum.NAME_ERROR
    else:
        my_game = Game(name=client_data.game_name, password=client_data.password, game_type=client_data.game_type,
                       owner_id=session_id)

        send_data.response_code = form.CreateGameEnum.SUCCESS
        send_data.game_id = my_game.game_id

    return send_data.__dict__


def handle_join_game(data, session_id):
    client_data = form.ClientJoinGame(data)
    send_data = form.ServerJoinGame()
    try:
        game = Game.Games[client_data.game_id]
        send_data.response_type = form.JoinGameEnum.WRONG_PASSWORD
        if game.password == client_data.password:
            player = Participant(session_id)
            game.add_participant(player)
            send_data.game_name = game.game_name
            send_data.response_type = form.JoinGameEnum.SUCCESS
    except KeyError:
        send_data.response_type = form.JoinGameEnum.NOT_EXIST

    return send_data.__dict__


def aggregate_lobby_list():
    d = {}
    for games in Game.Games.values():
        games: Game
        var = form.UpdateGameListVariables()
        var.game_name = games.game_name
        var.game_type = games.game_type
        var.owner = session.Session.sessions[games.owner_id].player_name
        var.num_players = games.num_present
        var.in_progress = str(games.in_progress)
        d[games.game_id] = var.__dict__
    return d


