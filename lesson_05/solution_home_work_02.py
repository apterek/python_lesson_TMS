import random


list_name = ['Dimas', 'Sasha', 'Petr', 'Stepan', 'Ann']
list_name1 = ['Dimas', 'Sasha', 'Petr', 'Stepan', 'Ann']


def generate_pull_list(number_users):
    number_users_pull = random.randint(0, number_users)
    return number_users_pull


def santa_game(bag_with_list):
    for name in list_name:
        while True:
            is_paper = bag_with_list[generate_pull_list(len(bag_with_list) - 1)]
            if name != is_paper:
                print(name, 'take a gift to ', is_paper)
                bag_with_list.remove(is_paper)
                break


list_pulls = santa_game(list_name1)

