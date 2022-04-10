import shared_directory.data_format as form
import session
from uuid import uuid4


class Participant:
    Participants = {}

    def __init__(self, session_id):
        self.session_id = session_id
        session_object: session.Session = session.Session.sessions[session_id]
        self.username = session_object.player_name
        self.Participants[session_id] = self


class Game:
    Games = {}

    def __init__(self, name, game_type, password, owner_id):
        self.present = []
        self.players = []
        self.owner_id = owner_id
        self.game_name = name
        self.game_type = game_type
        self.password = password
        self.in_progress = False
        self.game_status = form.GameStatus.INVALID
        self.game_id = self.create_game_id()
        self._add_game()
        self.add_participant(Participant(owner_id))

    @staticmethod
    def create_game_id():
        return str(uuid4())

    def _add_game(self):
        self.Games[self.game_id] = self

    @classmethod
    def lobby_name_exists(cls, session_id):
        if session_id in cls.Games:
            return True
        else:
            return False

    @classmethod
    def game_name_exists(cls, name):
        for game in cls.Games.values():
            game: Game
            if game.game_name == name:
                return True
        return False

    @classmethod
    def game_owner_exists(cls, session_id):
        for game in cls.Games.values():
            game: Game
            if game.owner_id == session_id:
                return True
        return False

    def add_participant(self, participant: Participant):
        self.present.append(participant)

    def remove_participant(self, participant: Participant):
        if participant in self.players:
            self.players.remove(participant)
        self.present.remove(participant)

    def add_player(self, participant: Participant):
        self.players.append(participant)

    def remove_player(self, participant: Participant):
        self.players.remove(participant)

    def player_present(self, participant: Participant):
        if participant in self.present:
            return True
        else:
            return False

    def remove_game(self):
        del self.Games[self.owner_id]

    @property
    def num_present(self):
        return len(self.present)

    @property
    def num_playing(self):
        return len(self.players)


