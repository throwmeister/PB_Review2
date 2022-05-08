import abc

import shared_directory.data_format as form
import session
import random
from server_info import ServerData
from uuid import uuid4
import pokerScoreCalculator as p_scoreCalc
import blackjackScoreCalculator as b_scoreCalc


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

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
        ServerData.logger.info(self.cards)

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
        self.hand = []
        self.deck = deck
        self.current_bet = 0
        self.has_bet = False
        self.all_in = False
        self.played = True

    @abc.abstractmethod
    def make_bet(self, amount_list):
        pass

    def get_cards_format(self):
        cards = []
        ServerData.logger.info(f'Cards: {self.hand}')
        for card in self.hand:
            cards.append(card.__dict__)
        return cards

    def set_all_in(self, all_in):
        if all_in == form.AllInEnum.YES:
            self.all_in = True

    # Draw from the deck
    def draw(self):
        self.hand.append(self.deck.draw())

    def remove(self, card):
        self.hand.remove(card)

    @abc.abstractmethod
    def calculate_player_score(self):
        pass


class PokerPlayerVariables(ParticipantVariables):
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

    def __init__(self, deck):
        self.has_replaced = False
        super().__init__(deck)

    def draw_cards(self):
        for _ in range(5):
            self.draw()

    def make_bet(self, amount_list):
        bet_sum = sum(amount_list)
        if bet_sum < self.current_bet:
            # Checks if the previous bet was higher (Poker only)
            return False
        self.current_bet = bet_sum
        ServerData.logger.info(f'Current bet: {self.current_bet}')
        self.has_bet = True
        return True

    def replace_cards(self, cards):
        try:
            for card in cards:
                card: Card
                # Gets the index of the card that should be replaced
                index = self.get_cards_format().index(card)
                self.hand.pop(index)
                self.draw()
            self.has_replaced = True
        except ValueError:
            ServerData.logger.info('Card error')

    def calculate_player_score(self):
        # Calculates the score of all players

        cards = p_scoreCalc.list_of_values(self.hand, self.card_access)
        num_score = p_scoreCalc.value_calc(cards)
        if num_score == 0:
            flush = p_scoreCalc.suit_calc(self.hand)
            num_score = p_scoreCalc.straight_calc(cards, flush)
            if num_score == 0:
                num_score = p_scoreCalc.high_calc(cards)

        else:
            pass
        ServerData.logger.info(f'Player score: {num_score}')
        return num_score


class Dealer(ParticipantVariables):
    card_access = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11
    }

    def make_bet(self, amount_list):
        pass

    def __init__(self, deck):
        super(Dealer, self).__init__(deck)
        self.draw_cards()

    def dealer_deal(self):
        formted_hand = b_scoreCalc.list_of_hand(self.hand, self.card_access)
        score = b_scoreCalc.calculate(formted_hand)
        print(score)
        if score < 17:
            self.draw()
            self.dealer_deal()

    def draw_cards(self):
        for _ in range(2):
            self.draw()

    def calculate_player_score(self):
        hand = b_scoreCalc.list_of_hand(self.hand, self.card_access)
        score = b_scoreCalc.calculate(hand)
        ServerData.logger.info(f'Player score: {score}')
        return score


class BlackjackPlayerVariables(ParticipantVariables):
    card_access = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11
    }

    def __init__(self, deck):
        super().__init__(deck)
        self.hold = False

    def draw_cards(self):
        for _ in range(2):
            self.draw()

    def player_hit(self):
        self.draw()

    def make_bet(self, amount_list):
        bet_sum = sum(amount_list)
        self.bet_list = amount_list
        self.current_bet = bet_sum
        ServerData.logger.info(f'Current bet: {self.current_bet}')
        self.has_bet = True
        return True

    def player_hold(self):
        self.hold = True

    def double(self):
        self.current_bet *= 2

    def calculate_player_score(self):
        hand = b_scoreCalc.list_of_hand(self.hand, self.card_access)
        score = b_scoreCalc.calculate(hand)
        ServerData.logger.info(f'Player score: {score}')
        return score


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
        self.game_status = form.GameStatus.STARTING
        self.game_id = self.create_game_id()
        self._add_game()
        self.add_participant(Participant(owner_id))
        self.game_logic = None

    @staticmethod
    def create_game_id():
        return str(uuid4())

    def delete(self):
        self.Games.pop(self.game_id)

    def initialise_game(self):
        self.game_status = form.GameStatus.IN_PROGRESS
        match self.game_type:
            case form.GameTypeEnum.POKER:
                self.game_logic = Poker(self)
            case form.GameTypeEnum.BLACKJACK:
                self.game_logic = Blackjack(self)
                dealer = Dealer(self.game_logic.deck)
                self.game_logic.inset_dealer(dealer)
        for player in self.players:
            player: Participant
            player.setup_game_vars(self.game_type, self.game_logic.deck)

    def reset_game(self):
        self.game_status = form.GameStatus.STARTING
        self.game_logic = None

    def _add_game(self):
        self.Games[self.game_id] = self

    @classmethod
    def lobby_name_exists(cls, game_name):
        for game in cls.Games.values():
            game: Game
            if game_name == game.game_name:
                return True
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
        self.deck = Deck(num_of_decks)
        self.player_scores = []
        self.state = form.GameState.SETUP
        self.has_bet = 0
        self.parent: Game = game_cls

    def set_state(self, state):
        self.state = state

    def check_all_bet(self):
        for player in self.parent.players:
            player: Participant
            if not player.vars.has_bet:
                return False
        return True

    def get_bet_values(self):
        d = []
        for player in self.parent.players:
            player: Participant
            d.append([player.username, player.vars.current_bet])
        return d

    def calculate_scores(self):
        for this_player in self.parent.players:
            score = this_player.vars.calculate_player_score()
            self.player_scores.append([this_player, score])

    @abc.abstractmethod
    def calculate_winner(self):
        pass


class Poker(GameVariables):
    def __init__(self, game_cls):
        super(Poker, self).__init__(1, game_cls)
        self.pot = 0

    def check_all_replaced(self):
        for player in self.parent.players:
            player: Participant
            if not player.vars.has_replaced:
                return False
        return True

    def reset_bet_vars(self):
        for player in self.parent.players:
            player: Participant
            player.vars.has_bet = False
            player.vars.current_bet = 0

    def add_bets_to_pot(self):
        for player in self.parent.players:
            self.pot += player.vars.current_bet

    def check_all_bets_equal(self):
        all_in_list = []

        for player in self.parent.players:
            player: Participant
            # self.bets.append(player.vars.current_bet)
            all_in_list.append([player.vars.current_bet, player.vars])
        bets = sorted(all_in_list, key=lambda x: x[0], reverse=True)
        # Gets all bets in order
        non_high_bets = [x[1] for x in bets if x[0] != bets[0][0]]
        # List comprehension - extract the players whose bets are not equal to the highest bet
        for player in non_high_bets:
            if not player.vars.all_in:
                return False
        return True

    def calculate_winner(self):
        # Sorts by highest score
        new = sorted(self.player_scores, key=lambda x: x[1], reverse=True)
        # List comprehension extracts all the winners
        winners = [p[0] for p in new if p[1] == new[0][1]]
        send_winners = []
        for winner in winners:
            # Calculates all the winners and gives them their money
            ServerData.logger.info(winner)
            earnt_money = self.pot / (len(winners))
            ServerData.logger.info(f'Earnt money: {earnt_money}')
            d = form.GameWinnerVars()
            d.winnings = earnt_money
            d.session = winner.session_id
            d.name = winner.username

            send_winners.append(d.__dict__)
        return send_winners


class Blackjack(GameVariables):
    def __init__(self, game_cls):
        super().__init__(5, game_cls)

    def check_all_hold(self):
        for player in self.parent.players:
            player: Participant
            if not player.vars.hold:
                return False
        return True

    def inset_dealer(self, dealer):
        self.dealer = dealer

    def calculate_winner(self):
        new = sorted(self.player_scores, key=lambda x: x[1], reverse=True)
        winners = []
        draw = []
        temp_winners = [p for p in new if p[1] <= 21]
        dealer_score = self.dealer.calculate_player_score()
        if dealer_score <= 21:
            winners = [p[0] for p in temp_winners if p[1] >= dealer_score]
            draw = [p[0] for p in temp_winners if p[1] == dealer_score]
        else:
            winners = [p[0] for p in temp_winners]

        send_winners = []
        for winner in winners:
            winner: Participant
            if winner in draw:
                earnt_money = winner.vars.current_bet
            else:
                earnt_money = winner.vars.current_bet * 2
            d = form.GameWinnerVars()
            d.winnings = earnt_money
            d.session = winner.session_id
            d.name = winner.username

            send_winners.append(d.__dict__)

        return send_winners




'''
    def set_logic(self):
        if self.game_type == form.GameTypeEnum.POKER:
            Poker()
        elif self.game_type == form.GameTypeEnum.BLACKJACK:
            Blackjack()
'''
