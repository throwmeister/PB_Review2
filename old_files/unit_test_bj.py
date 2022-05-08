import games_logic as logic

import pokerScoreCalculator as p_calc

import blackjackScoreCalculator as b_calc


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


bj_card_access = {
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


class Dealer:
    def __init__(self):
        card1 = Card('Hearts', 2)
        card3 = Card('Spades', 10)

        self.hand = [card3, card1]

    def hit(self):
        self.hand.append(Card('Hearts', 5))

    def dealer_deal(self):
        formted_hand = b_calc.list_of_hand(self.hand, bj_card_access)
        score = b_calc.calculate(formted_hand)
        print(score)
        if score < 17:
            self.hit()
            self.dealer_deal()



#card1 = Card('Hearts', 10)
#card2 = Card('Hearts', 'Ace')
#card3 = Card('Spades', 10)

dealer = Dealer()
dealer.dealer_deal()
print(dealer.hand)

#hand = [card2, card3, card1]
#formted_hand = b_calc.list_of_hand(hand, bj_card_access)
#print(b_calc.calculate(formted_hand))


#card3 = Card('Hearts', 10)
#card4 = Card('Hearts', 10)