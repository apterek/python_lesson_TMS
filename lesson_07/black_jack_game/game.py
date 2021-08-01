from gen_deck_cards import gen_big_deck
from gen_card import gen_card_score
from gen_card import pull_random_card
from tabulate import tabulate
from pprint import pprint


names_players_of_the_table = ['croupier']


def game(names_of_players, deck_quantity=1):
    players_table_score = {name: 0 for name in names_of_players}
    deck = gen_big_deck(deck_quantity)
    for key, value in players_table_score.items():
        for _ in range(2):
            card = pull_random_card(deck.keys())


game(names_players_of_the_table)













