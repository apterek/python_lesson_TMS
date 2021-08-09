import random


def pull_random_card(card_deck):
    cards = [card for card in card_deck]
    random_card = cards[random.randint(0, len(cards) - 1)]
    return random_card


def gen_card_score(card):
    cards_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 2, 'D': 3, 'K': 4, 'A': 11
    }
    return cards_values.get(card)
