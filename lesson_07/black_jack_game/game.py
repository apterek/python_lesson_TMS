from gen_deck_cards import gen_big_deck
from gen_card import gen_card_score
from gen_card import pull_random_card


names_of_players = ['croupier', 'dima', 'slava']


def check(players_table_score_1, deck_1, key_1):
    while True:
        card = pull_random_card(deck_1.keys())
        if deck_1.get(card) == 0:
            pass
        else:
            deck_1[card] = deck_1.get(card) - 1
            break
    players_table_score_1[key_1] = \
        int(players_table_score_1.get(key_1)) + gen_card_score(card.split(':')[0])
    return players_table_score_1, deck_1


def game(players_table_score, deck):
    # The first distribution
    for key in players_table_score.keys():
        for _ in range(2):
            players_table_score, deck = check(players_table_score, deck, key)
    # Players are playing
    for key in players_table_score:
        if key == 'croupier':
            continue
        while True:
            print(f'Plays player |{key}|: ')
            if players_table_score.get(key) == 21:
                print(f'You have BlackJack, your score: |{players_table_score.get(key)}|,'
                      f' wait for the result in others players')
                break
            if input(f'Your score: |{players_table_score.get(key)}|,'
                        f'if you want to continue enter yes: ') == 'yes':
                players_table_score, deck = check(players_table_score, deck, key)
                if players_table_score.get(key) > 21:
                    print(f"Your score: |{players_table_score.get(key)}|,"
                          f" you have too many points, YOU LOSE")
                    break
            else:
                print(f'Your score: {players_table_score.get(key)}')
                break
    # Players are croupier
    scores = players_table_score.get('croupier')
    while True:
        print(f"croupier take a cards, current score croupier:"
              f" {players_table_score.get('croupier')}")
        if players_table_score.get('croupier') == 21:
            print(f"croupier have a BlackJack")
        players_table_score, deck = check(players_table_score, deck, 'croupier')
        if players_table_score.get('croupier') > 21:
            break
    print(players_table_score)


deck_quantity = 1  # make input()
deck_with_card = gen_big_deck(deck_quantity)
table_score = {name: 0 for name in names_of_players}
game(table_score, deck_with_card)



