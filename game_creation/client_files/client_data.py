from game_creation.shared_directory import data_format as form


class ClientInfo:
    username = ''
    keep_alive = 0
    session_id = ''
    game_id = ''
    game_owner = False
    valid_session = False
    playing = False

    message_queue = None
    tcpHandler = None
    main_gui = None
    login_gui = None
    create_game_gui = None
    join_gui = None
    bet_gui = None
    logger = None

    @classmethod
    def set_login_values(cls, username, keepalive, session_id):
        cls.username = username
        cls.keep_alive = keepalive
        cls.session_id = session_id


class GameInfo:
    bet = 100
    request = True
    state = form.GameState.SETUP
    game_type = form.GameTypeEnum.UNKNOWN
    replace_list = []

    @classmethod
    def set_initial_values(cls, gtype):
        cls.state = form.GameState.BETTING
        cls.replace_list = []
        cls.game_type = gtype
        cls.request = True
