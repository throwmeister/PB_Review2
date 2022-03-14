class ServerConfig:
    @staticmethod
    def activity_timeout():
        return 60

    @staticmethod
    def keep_alive():
        return 20

    @staticmethod
    def db_path():
        return 'data/game_server_db.db'

    @staticmethod
    def decode_format():
        return 'utf-8'
