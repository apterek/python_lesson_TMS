import random


cards = [
    '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
]

suits = [
    'Hearts', 'Diamonds', 'Clubs', 'Spades'
]
cards_value = {
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'D': 3, 'K': 4, 'A': 11
}


# generate random card
def pull_random_card(cards_sequences, suit_sequences):
    random_card = {cards_sequences[random.randint(0, len(cards_sequences) - 1)]: suit_sequences[
        random.randint(0, len(suit_sequences) - 1)]}
    return random_card


def black_jack():
    sum_cards = 0
    # Start game
    while True:
        pull_card = {}
        last_card = {}
        # pull unique card
        while True:
            pull_card = pull_random_card(cards, suits)
            if pull_card == last_card:
                continue
            else:
                last_card = pull_card
                break
        # take card
        card = cards_value[list(pull_card.keys())[0]]
        # check value card A
        if card == 11 and sum_cards+11 > 21:
            card = 1
        # score
        sum_cards += card
        print(f'You scored {sum_cards} points')
        # if score > max value
        if sum_cards > 21:
            return print(f'you score {sum_cards}, game end, YOU LOSE !!!')
        elif sum_cards == 21:
            return print(f'you score {sum_cards}, game end')
        # pull more card
        game_continue = input('Enter | yes |  if you want to take another card: ')
        # check game continue
        if game_continue != 'yes':
            return print(f'you score {sum_cards}, game end')


black_jack()


