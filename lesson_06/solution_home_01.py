line = 'Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. \
        реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, \
        в случае положительного ответа  - вытягивать случайную карту.реализовать.  \
        Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го. карту'


# remove points, commas, and characters less than two from original line
def change_line(input_line):
    # remove points, commas and convert sting to list
    inputs_line = input_line.replace('.', ' ').replace(',', ' ').split()
    # remove characters less than two
    new_line1 = list(filter(lambda row: len(row) > 2, inputs_line))

    return new_line1


# find the longest word, return list (of several same length)
def word_max(lines):
    # find length the longest word
    max_arg = max(list(map(lambda wrd: len(wrd), lines)))
    # return longest words
    words_with_max_len = list(filter(lambda rows: max_arg == len(rows), lines))

    return ' '.join(words_with_max_len)


# find the two most occurring words
def max_repeat_word(unique_line, true_line):
    maximum_word = {}
    # create a dictionary with unique words and the values occurring of these words in the text
    for line_1 in unique_line:
        previous_value = 0
        for line_2 in true_line:
            if line_1 == line_2:
                previous_value += 1
        maximum_word[line_1] = previous_value
    # return list with two most occurring words
    # sorting dictionary by values
    words = sorted(maximum_word, key=lambda x: maximum_word.get(x), reverse=True)[0:2]
    # check two most occurring words
    for key, value in maximum_word.items():
        if key == words[0] and value == 1:
            words = 'All words occur in string by 1 times'
        elif key == words[1] and value == 1:
            words[1] = 'All others words occur in string by 1 times'

    return ', '.join(words)


unique_list = list(set(change_line(line)))
print('The longest word: ', word_max(unique_list))
print('The two most occurring words: ', max_repeat_word(unique_list, change_line(line)))
