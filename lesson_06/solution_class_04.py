import random

cards = [
    '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
]
suit = [
    'Hearts', 'Diamonds', 'Clubs', 'Spades'
]
cards_value = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'D': 3, 'K': 4, 'A': 11}
cards_value = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'D': 3, 'K': 4, 'A': 11}


def pull_random_card(cards_sequences, suit_sequences):
    random_card = {cards_sequences[random.randint(0, len(cards_sequences) - 1)]: suit_sequences[
        random.randint(0, len(suit_sequences) - 1)]}
    return random_card


def black_jack():
    sum_card = 0
