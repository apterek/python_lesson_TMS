line = 'Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. \
        реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, \
        в случае положительного ответа  - вытягивать случайную карту.  \
        Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го. карту'


def change_line(input_line):
    inputs_line = input_line.replace('.', ' ').replace(',', ' ').split()
    new_line1 = list(filter(lambda row: len(row) > 2, inputs_line))

    return new_line1


def word_max(lines):
    max_arg = max(list(map(lambda wrd: len(wrd), lines)))
    words_with_max_len = list(filter(lambda rows: max_arg == len(rows), lines))

    return words_with_max_len


def max_repeat_word(unique_line, true_line):
    maximum_word = {}
    for line_1 in unique_line:
        previous_value = 0
        for line_2 in true_line:
            if line_1 == line_2:
                previous_value += 1
        maximum_word[line_1] = previous_value
    new_dict = {

    }

    print(maximum_word)


unique_list = list(set(change_line(line)))
print(word_max(unique_list))
max_repeat_word(unique_list, change_line(line))

