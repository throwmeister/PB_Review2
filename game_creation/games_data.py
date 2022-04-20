import shared_directory.data_format as form
import session
import random
from uuid import uuid4
import pokerScoreCalculator as p_scoreCalc


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display(self):
        print(f'{self.value} of {self.suit}')

    def return_card(self):
        return f'{self.value} of {self.suit}'

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def __str__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self, num, game_type=Card):
        self.cards = []
        self.game_type = game_type
        self.build(num)

    def build(self, num):
        # Create the deck
        for _ in range(num):
            for suit in ['Spades', 'Diamonds', 'Clubs', 'Hearts']:
                for j in range(2, 11):
                    self.cards.append(self.game_type(suit, j))
                for i in ['Jack', 'Queen', 'King', 'Ace']:
                    self.cards.append(self.game_type(suit, i))
        random.shuffle(self.cards)
        print(self.cards)

    def display(self):
        # Displays each card individually
        for card in self.cards:
            card.display()

    def draw(self):
        # Draw cards from the deck
        return self.cards.pop()

    def show_card(self, val):
        # Shows a specific card value
        self.cards[val].display()


class Participant:
    Participants = {}

    def __init__(self, session_id):
        self.session_id = session_id
        session_object: session.Session = session.Session.sessions[session_id]
        self.username = session_object.player_name
        self.Participants[session_id] = self
        self.playing = False
        self.vars = None

    def setup_game_vars(self, gtype, deck):
        if gtype == form.GameTypeEnum.POKER:
            self.vars = PokerPlayerVariables(deck)
            self.vars.draw_cards()
            self.vars: PokerPlayerVariables
        elif gtype == form.GameTypeEnum.BLACKJACK:
            self.vars = BlackjackPlayerVariables(deck)
            self.vars.draw_cards()
            self.vars: BlackjackPlayerVariables


class ParticipantVariables:
    def __init__(self, deck):
        self.money = 100
        self.hand = []
        self.deck = deck
        self.prev_bets = 0

    def make_bet(self, amount):
        amount -= self.prev_bets
        self.money -= amount
        self.prev_bets = amount

    def get_cards_format(self):
        cards = []
        print(self.hand)
        for card in self.hand:
            cards.append(card.__dict__)
        return cards

    def add_money(self, amount):
        self.money += amount

    def draw(self):
        self.hand.append(self.deck.draw())

    def remove(self, card):
        self.hand.remove(card)


class PokerPlayerVariables(ParticipantVariables):
    def __init__(self, deck):
        self.has_replaced = False
        super().__init__(deck)

    def draw_cards(self):
        for _ in range(5):
            print('card has been drawn')
            self.draw()

    def replace_cards(self, cards):
        try:
            for card in cards:
                card: Card
                index = self.get_cards_format().index(card)
                self.hand.pop(index)
                self.draw()
            self.has_replaced = True
        except ValueError:
            print('Error with cards')

    def calculate_player_score(self):
        # Calculates the score of all players

        card_access = {
            '3': 3,
            '2': 2,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14
        }
        cards = p_scoreCalc.list_of_values(self.hand, card_access)
        num_score = p_scoreCalc.value_calc(cards)
        if num_score == 0:
            flush = p_scoreCalc.suit_calc(self.hand)
            num_score = p_scoreCalc.straight_calc(cards, flush)
            if num_score == 0:
                num_score = p_scoreCalc.high_calc(cards)

        else:
            pass
        print(num_score)
        return num_score


class BlackjackPlayerVariables(ParticipantVariables):
    def __init__(self, deck):
        super().__init__(deck)
        self.hold = False

    def draw_cards(self):
        for _ in range(2):
            self.draw()

    def add_card(self):
        pass


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
        self.game_logic = None

    @staticmethod
    def create_game_id():
        return str(uuid4())

    def initialise_game(self):
        match self.game_type:
            case form.GameTypeEnum.POKER:
                self.game_logic = Poker(self)
                self.game_logic: Poker
            case form.GameTypeEnum.BLACKJACK:
                self.game_logic = Blackjack(self)
                self.game_logic: Blackjack
        for player in self.players:
            player: Participant
            player.setup_game_vars(self.game_type, self.game_logic.deck)

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


class GameVariables:
    def __init__(self, num_of_decks, game_cls):
        self.pot = 0
        self.deck = Deck(num_of_decks)
        self.player_scores = []
        self.state = form.GameState.SETUP
        self.has_bet = 0
        self.parent: Game = game_cls

    def set_state(self, state):
        self.state = state

    def add_to_pot(self, amount):
        self.pot += amount

    def calculate_scores(self):
        pass

    def calculate_winner(self):
        winners = []
        duple = 0
        # A counter for if there is more than one winner
        new = sorted(self.player_scores, key=lambda x: x[1], reverse=True)
        while True:
            # Logic to check for multiple winners
            try:
                if new[duple][1] == new[duple + 1][1]:
                    duple += 1
                else:
                    break
            except IndexError:
                break
        for i in range(duple + 1):
            # Calculates all the winners and gives them their money
            winner = new[i][0]
            print(winner)
            earnt_money = self.pot / (duple + 1)
            winner.vars.add_money(earnt_money)
            d = form.GameWinnerVars()
            d.winnings = earnt_money
            d.session = winner.session_id
            d.name = winner.username

            winners.append(d.__dict__)
        return winners


class Poker(GameVariables):
    def __init__(self, game_cls):
        super(Poker, self).__init__(1, game_cls)

    def check_all_replaced(self):
        for player in self.parent.players:
            player: Participant
            if not player.vars.has_replaced:
                return False
        return True

    def calculate_scores(self):
        for this_player in self.parent.players:
            score = this_player.vars.calculate_player_score()
            self.player_scores.append([this_player, score])


class Blackjack(GameVariables):
    def __init__(self, game_cls):
        super().__init__(5, game_cls)


'''
    def set_logic(self):
        if self.game_type == form.GameTypeEnum.POKER:
            Poker()
        elif self.game_type == form.GameTypeEnum.BLACKJACK:
            Blackjack()
'''
