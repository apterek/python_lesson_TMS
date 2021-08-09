from gen_card import gen_card_score, pull_random_card


def check(players_table_score_1, deck_1, key_1):
    while True:
        card = pull_random_card(deck_1.keys())
        card_value = gen_card_score(card.split(':')[0])
        # if pull A, choice value A
        if players_table_score_1.get(key_1) > 10 and card_value == 11:
            card_value = 1
        if deck_1.get(card) == 0:
            pass
        else:
            deck_1[card] = deck_1.get(card) - 1
            break
    players_table_score_1[key_1] = \
        int(players_table_score_1.get(key_1)) + card_value
    return players_table_score_1, deck_1
