import csv


def open_csv(filename):
    new_dict = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            key, value = row
            new_dict[key] = value
    return new_dict


def translate_ru_eng(word):
    for key, value in dict_ru_to_eng .items():
        if value == word:
            return key


def translate_eng_ru(word):
    for key, value in dict_eng_to_rus.items():
        if value == word:
            return key


dict_ru_to_eng = open_csv('solution_02.csv')
dict_eng_to_rus = {
    value: key
    for key, value in dict_ru_to_eng.items()
}


print(translate_ru_eng('routing'))
print(translate_eng_ru('кот'))


