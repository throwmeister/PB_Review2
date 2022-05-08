def list_of_hand(hand, card_access):
    cards = []
    for card in hand:
        value = card_access[str(card.get_value())]
        cards.append(value)
    return cards


def calculate(hand):
    score = sum(hand)

    if score > 21 and 11 in hand:
        hand.remove(11)
        # Recursion
        hand.append(1)
        return calculate(hand)
    else:
        return score

