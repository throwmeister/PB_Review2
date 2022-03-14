from datetime import datetime, timezone
import time
from configuration_protocol import ServerConfig
import uuid


class Session:
    sessions = []

    def __init__(self, name):
        self._username = name
        self._last_activity = None
        self._sessionID = self._createID()
        self._last_activity_time = self.current_time()
        self.sessions.append(self)

    def _createID(self):
        # Generate session ID
        return uuid.uuid4()

    def current_time(self):
        time_secs = datetime.now(timezone.utc).timestamp()
        return time_secs

    def is_validate_session(self):
        return self.activity_time < ServerConfig.activity_timeout()

    @property
    def activity(self):
        return self._last_activity

    @property
    def ID(self):
        return self._sessionID

    @property
    def player_name(self):
        return self._username

    @property
    def activity_time(self):
        print('getting...')
        timer = self.current_time() - self._last_activity_time
        return timer

    @classmethod
    def get_session(cls, username):
        for session in cls.sessions:
            if username == session.player_name:
                return session
            else:
                return None


if __name__ == '__main__':
    x = Session('alex')
    f = Session('john')
    getting = x.activity_time
    time.sleep(3)


    print(Session.sessions)
    c = Session.session_exists('john')


