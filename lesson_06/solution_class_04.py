import random
import re

cards = [
    '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
]
suits = [
    'Hearts', 'Diamonds', 'Clubs', 'Spades'
]
cards_value = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'D': 3, 'K': 4, 'A': 11}


def pull_random_card(cards_sequences, suit_sequences):
    random_card = {cards_sequences[random.randint(0, len(cards_sequences) - 1)]: suit_sequences[
        random.randint(0, len(suit_sequences) - 1)]}
    return random_card


def black_jack():
    sum_cards = 0
    while True:
        card = cards_value[list(pull_random_card(cards, suits).keys())[0]]
        if card == 11 and sum_cards+11 > 21:
            card = 1
        sum_cards += card
        print(f'You scored {sum_cards} points')
        game_continue = input('Enter | yes |  if you want to take another card: ')
        if game_continue != 'yes' or sum_cards >= 21:
            print(f'you score {sum_cards}, game end')
            break


black_jack()

