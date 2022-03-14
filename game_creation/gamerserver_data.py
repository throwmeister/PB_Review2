import sqlite3
from configuration_protocol import ServerConfig


class DBManager:

    def __init__(self):
        pass
        '''
        connection = sqlite3.connect('data/game_server_db.db')
        cursor = connection.cursor()

        cursor.execute('SELECT Username, Password FROM users')
        print(cursor.fetchall())

        connection.close()
        '''

    def get_user(self, username):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT Username, Password FROM users WHERE Username = '{username}'")
        result = cursor.fetchall()
        connection.close()
        return result

    @staticmethod
    def get_connection():
        return sqlite3.connect(ServerConfig.db_path())


if __name__ == '__main__':
    x = DBManager()
    r = x.get_user('Alex')
    tester_tuple_list = [('john', 'bomb'), ('fomb', 'lomb')]
    print(r)
    f, g = zip(*r)
    print(*f)
    print(*g)
    a, b = zip(*tester_tuple_list)
    print(*a)
    print(*b)