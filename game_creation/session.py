from datetime import datetime, timezone
import time
from configuration_protocol import ServerConfig
import uuid


class Session:
    sessions = {}

    def __init__(self, name):
        self._username = name
        self._last_activity_done = None
        self._session_id = self._createID()
        self._last_activity_time = self.current_time()
        self.sessions[self._session_id] = self

    def _createID(self):
        # Generate session ID - must have it as a string as you can't serialise a uuid value
        return str(uuid.uuid4())

    def current_time(self):
        time_secs = datetime.now(timezone.utc).timestamp()
        return time_secs

    def is_validate_session(self):
        return self.activity_time < ServerConfig.activity_timeout()

    @property
    def activity(self):
        return self._last_activity_done

    def update_activity(self):
        print('Updated')
        self._last_activity_time = self.current_time()

    @property
    def ID(self):
        return self._session_id

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
        for session in cls.sessions.values():
            if username == session.player_name:
                return session
            else:
                return None

    @classmethod
    def validate_session(cls, session_id):
        if session_id in cls.sessions:
            this_session: Session = cls.sessions[session_id]
            this_session.update_activity()
            return True
        else:
            return False

    @classmethod
    def delete_session(cls, session_id):
        this_session: Session = cls.sessions[session_id]
        print(this_session)
        this_session.remove_session()

    def remove_session(self):
        del self.sessions[self._session_id]


def create_session(username):
    # Logic - if somehow the user crashes and the session is not cleared, there will be only one outstanding session
    # Therefore, there is no need to search for more than one existing session because it will not allow more than 1 to
    # Run at one time
    existing_session = Session.get_session(username)
    if existing_session:
        if existing_session.activity_time < 60:
            # Active session already exists
            return None
        else:
            existing_session.remove_session()
    return Session(username)


if __name__ == '__main__':
    x = Session('alex')
    f = Session('john')
    getting = x.activity_time
    time.sleep(3)
    print(Session.sessions)
    c = Session.get_session('alex')
    print(c.activity_time)


