import builtins
import session
from games_data import Game, Participant
import shared_directory.data_format as form
from gamerserver_data import DBManager
from configuration_protocol import ServerConfig
from server_info import ServerData


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
                ServerData.logger.info('Login already exists')
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
    if session_id:
        session.Session.delete_session(session_id)


def handle_create_game(data, session_id):
    client_data = form.ClientCreateGame(data)
    send_data = form.ServerCreateGame()

    if Game.game_owner_exists(session_id):
        send_data.response_code = form.CreateGameEnum.ALREADY_CREATED_GAME

    elif Game.lobby_name_exists(client_data.game_name):
        # raise error
        send_data.response_code = form.CreateGameEnum.NAME_ERROR
    else:
        my_game = Game(name=client_data.game_name, password=client_data.password, game_type=client_data.game_type,
                       owner_id=session_id)

        send_data.response_code = form.CreateGameEnum.SUCCESS
        send_data.game_id = my_game.game_id

    return [send_data.__dict__, send_data.game_id]


def handle_join_game(data, session_id):
    client_data = form.ClientJoinGame(data)
    send_data = form.ServerJoinGame()
    try:
        game = Game.Games[client_data.game_id]
        send_data.response_code = form.JoinGameEnum.WRONG_PASSWORD
        if session_id == game.owner_id:
            send_data.response_code = form.JoinGameEnum.JOIN_ITSELF
        elif game.password == client_data.password:
            player = Participant(session_id)
            game.add_participant(player)
            send_data.game_name = game.game_name
            send_data.response_code = form.JoinGameEnum.SUCCESS
            send_data.game_id = game.game_id
    except KeyError:
        send_data.response_code = form.JoinGameEnum.NOT_EXIST
    ServerData.logger.info(f'game id: {send_data.game_id}, {client_data.game_id}')
    return [send_data.__dict__, client_data.game_id]


def handle_leave_game(game_id, session_id):
    try:
        game = Game.Games[game_id]
        participant = Participant.Participants[session_id]
        if participant in game.players:
            game.remove_player(participant)
        game.remove_participant(participant)
        if not game.players:
            ServerData.logger.info('Game deleted')
            game.delete()
    except KeyError:
        pass


def handle_ready_game(data, session_id):
    client_data = form.ClientReadyGame(data)
    send_data = form.ServerReadyResponse()
    send_data.response_type = client_data.request
    ServerData.logger.info(f'Client request: {send_data.response_type}')
    try:
        game = Game.Games[client_data.game_id]
        player = Participant.Participants[session_id]
        if game.player_present(player):
            ServerData.logger.info('Player is present')
            send_data.response_code = form.ReadyResponseEnum.SUCCESS
            if client_data.request == form.ReadyTypeEnum.READY:
                ServerData.logger.info('Player is readying')
                game.add_player(player)
            elif client_data.request == form.ReadyTypeEnum.UNREADY:
                ServerData.logger.info('Player is unreadying')
                game.remove_player(player)
            else:
                send_data.response_code = form.ReadyResponseEnum.ERROR
        else:
            send_data.response_code = form.ReadyResponseEnum.ERROR
            ServerData.logger.info('Player is not present')
    except KeyError:
        ServerData.logger.info('Key error')

    return [send_data.__dict__, client_data.game_id]


def game_request_validation(session_id, game_id):
    try:
        game = Game.Games[game_id]
        player = Participant.Participants[session_id]
        if player in game.players:
            return [game, player]
        else:
            return False
    except KeyError:
        return False


def handle_start_game(data, session_id):
    client_data = form.ClientStartGame(data)
    send_data = form.ServerStartResponse()

    def error():
        send_data.response_code = form.GeneralEnum.ERROR
    try:
        game = Game.Games[client_data.game_id]
        if game.owner_id == session_id:
            send_data.response_code = form.GeneralEnum.SUCCESS
            send_data.game_type = game.game_type
            begin_game(game)
        else:
            ServerData.logger.info('Not the owner')
            error()
    except KeyError:
        ServerData.logger.info('Key error')
        error()

    return [send_data.__dict__, client_data.game_id]


def begin_game(game_instance: Game):
    game_instance.initialise_game()
    game_instance.game_logic.set_state(form.GameState.BETTING)


def get_bets(game_id):
    game = Game.Games[game_id]
    return game.game_logic.get_bet_values()


def handle_input_bet(data, session_id):
    client_data = form.ClientSendBet(data)
    send_data = form.ServerBetResponse()
    complete = False
    pv_checker = game_request_validation(session_id, client_data.game_id)
    if pv_checker:
        game, player = pv_checker
        player: Participant
        game: Game
        bet_result = player.vars.make_bet(client_data.bet)
        if bet_result:
            player.vars.set_all_in(client_data.all_in)
            if check_betting_complete(game):
                complete = True
            send_data.response_code = form.GeneralEnum.SUCCESS
        else:
            send_data.response_code = form.GeneralEnum.ERROR
    else:
        send_data.response_code = form.GeneralEnum.ERROR

    return [send_data.__dict__, client_data.game_id, complete]


def check_betting_complete(game):
    complete = False
    if game.game_logic.check_all_bet() and game.game_logic.check_all_bets_equal():
        if game.game_logic.state == form.GameState.BETTING:
            game.game_logic.set_state(form.GameState.CARD_CHANGING)
            game.game_logic.add_bets_to_pot()
            game.game_logic.reset_bet_vars()
        elif game.game_logic.state == form.GameState.BETTING_TWO:
            game.game_logic.set_state(form.GameState.CALCULATED)
            game.game_logic.add_bets_to_pot()
        complete = True
    return complete


def get_cards(game_id, session_id):
    send_data = form.ServerGetCards()
    pv_checker = game_request_validation(session_id, game_id)
    if pv_checker:
        game, player = pv_checker
        player: Participant
        game: Game
        cards = player.vars.get_cards_format()
        send_data.response_code = form.GeneralEnum.SUCCESS
        send_data.cards = cards
    else:
        send_data.response_code = form.GeneralEnum.ERROR

    return send_data.__dict__


def replace_cards(data, session_id):
    # Poker only command
    client_data = form.ClientSendCards(data)
    send_data = form.ServerGetCards()
    pv_checker = game_request_validation(session_id, client_data.game_id)
    complete = False
    if pv_checker:
        game, player = pv_checker
        player: Participant
        game: Game
        player.vars.replace_cards(client_data.cards)
        cards = player.vars.get_cards_format()
        send_data.cards = cards
        send_data.response_code = form.GeneralEnum.SUCCESS
        if game.game_type == form.GameTypeEnum.POKER:
            if game.game_logic.check_all_replaced():
                ServerData.logger.info('All players have replaced')
                complete = True
                game.game_logic.state = form.GameState.BETTING_TWO

    else:
        send_data.response_code = form.GeneralEnum.ERROR

    return [send_data.__dict__, client_data.game_id, complete]


def handle_hit_request(session_id, game_id):
    pv_checker = game_request_validation(session_id, game_id)
    complete = False
    send_data = form.ServerHitResponse()
    send_data.response_code = form.HitEnum.INVALID_REQUEST
    if pv_checker:
        game, player = pv_checker
        player: Participant
        game: Game
        if not player.vars.hold:
            player.vars.player_hit()
            score = player.vars.calculate_player_score()
            if score > 21:
                send_data.response_code = form.HitEnum.BUST
                player.vars.player_hold()
            else:
                send_data.response_code = form.HitEnum.HIT_SUCCESS
            send_data.cards = player.vars.get_cards_format()

            if game.game_logic.check_all_hold():
                ServerData.logger.info('All players are done')
                complete = True

    return [send_data.__dict__, complete]


def handle_hold_request(session_id, game_id):
    pv_checker = game_request_validation(session_id, game_id)
    complete = False
    send_data = form.ServerHoldResponse()
    send_data.response_code = form.GeneralEnum.ERROR
    if pv_checker:
        game, player = pv_checker
        player: Participant
        game: Game
        if not player.vars.hold:
            player.vars.player_hold()
            send_data.response_code = form.GeneralEnum.SUCCESS

        if game.game_logic.check_all_hold():
            ServerData.logger.info('All players done')
            complete = True

    return [send_data.__dict__, complete]


def calculate_game_score(game_id):
    game = Game.Games[game_id]
    game.game_logic.calculate_scores()
    winners = game.game_logic.calculate_winner()

    return winners


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


def aggregate_player_list(game_id):
    ServerData.logger.info(f'Game: {game_id}')
    try:
        game = Game.Games[game_id]
        d = []
        for player in game.present:
            player: Participant
            var = form.UpdatePlayerList()
            var.player_name = player.username
            if player in game.players:
                var.ready = form.PlayerReadyEnum.TRUE
            d.append(var.__dict__)
        return d
    except KeyError:
        pass


def aggregate_blackjack_list(game_id):
    game = Game.Games[game_id]
    # Player - card
    d = []
    for player in game.players:
        player_data = form.BlackjackCardPlayerVars()
        player_data.player_name = player.username
        player_data.card = player.vars.hand[0].__dict__
        d.append(player_data.__dict__)

    return d