import pokerScoreCalculator as p_scoreCalc


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

card1 = Card('Hearts', 10)
card2 = Card('Hearts', 'Jack')
card3 = Card('Hearts', 'King')
card4 = Card('Hearts', 'Ace')
card5 = Card('Hearts', 'Queen')
hand = [card1, card2, card3, card4, card5]


cards = p_scoreCalc.list_of_values(hand, card_access)
num_score = p_scoreCalc.value_calc(cards)
if num_score == 0:
    flush = p_scoreCalc.suit_calc(hand)
    num_score = p_scoreCalc.straight_calc(cards, flush)
    if num_score == 0:
        num_score = p_scoreCalc.high_calc(cards)

else:
    pass
print(num_score)
