name_of_cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
]
name_of_suits = [
    'Hearts', 'Diamonds', 'Clubs', 'Spades'
]


def gen_big_deck(number_of_deck=1):
    big_deck = {}
    for card in name_of_cards:
        for suit in name_of_suits:
            big_deck[f'{card}:{suit}'] = int(number_of_deck)
    return big_deck
