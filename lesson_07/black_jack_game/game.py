from gen_deck_cards import gen_big_deck
from chek_card import check


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

    # The croupier is playing
    while True:
        print(f"croupier take a cards, current score croupier:"
              f" {players_table_score.get('croupier')}")
        if players_table_score.get('croupier') == 21:
            print(f"croupier have a BlackJack")
            break
        players_table_score, deck = check(players_table_score, deck, 'croupier')
        if players_table_score.get('croupier') > 21:
            print(f"croupier take a cards, current score croupier:"
                  f" {players_table_score.get('croupier')}")
            break
    print(players_table_score)


if __name__ == '__main__':
    names_of_players = ['croupier']
    deck_quantity = int(input('Enter deck quantity(1-8): '))
    deck_with_card = gen_big_deck(deck_quantity)
    number_of_player = input("Enter number of players(1-7): ")
    while True:
        names_of_players.append(input("Enter names of players: "))
        if len(names_of_players) == int(number_of_player) + 1:
            break
    table_score = {name: 0 for name in names_of_players}
    game(table_score, deck_with_card)
