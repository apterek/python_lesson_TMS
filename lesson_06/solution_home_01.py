line = 'Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е.' \
       ' реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту,' \
       ' в случае положительного ответа  - вытягивать случайную карту. ' \
       'Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го. карту'


def change_line(input_line):
    inputs_line = input_line.replace('.', ' ').replace(',', ' ').split()
    new_line1 = []
    for row in inputs_line:
        if len(row) > 2:
            new_line1.append(row)
    return new_line1


def word_max(lines):
    max_arg = max(list(map(lambda wrd: len(wrd), lines)))
    for index_i, rows in enumerate(lines):
        if max_arg == index_i:
            return rows


def find_word(lines):
    list_m = []
    for word_in_line in lines:
        find_wordless = 0
        for i in lines:
            if word_in_line == i:
                find_wordless += 1
        list_m.append(find_wordless)
    return list_m


print(word_max(change_line(line)))
print(find_word(change_line(line)))
