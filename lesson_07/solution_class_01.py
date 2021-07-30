import random

cards = [
    '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
]
suit = [
    'Hearts', 'Diamonds', 'Clubs', 'Spades'
]


def pull_random_card(cards_sequences, suit_sequences):
    random_card = {cards_sequences[random.randint(0, len(cards_sequences) - 1)]: suit_sequences[
        random.randint(0, len(suit_sequences) - 1)]}
    return random_card


if __name__ == '__main__':
    print(pull_random_card(cards, suit))
