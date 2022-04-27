import games_logic as logic
import blackjackScoreCalculator as b_calc
import pokerScoreCalculator as p_calc
import cardAndDeck as card

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

card1 = card.Card('Clubs', 'Ace')
card2 = card.Card('Hearts', 10)
# card2 = card.Card('Spades', 'Ace')
card3 = card.Card('Hearts', 10)
card4 = card.Card('Hearts', 10)
hand = [card1, card2, card3, card4]
formted_hand = b_calc.list_of_hand(hand, bj_card_access)
print(b_calc.calculate(formted_hand))
