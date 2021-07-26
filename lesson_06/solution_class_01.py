vocabulary_dict = {'cat': 'кот',
                   'vocabulary': 'словарь',
                   'routing': 'маршрутизация'}


revers_dict = {
    value: key
    for key, value in vocabulary_dict.items()
}


def translate_ru_eng(word):
    for key, value in vocabulary_dict.items():
        if value == word:
            return key


def translate_eng_ru(word):
    for key, value in revers_dict.items():
        if value == word:
            return key


print(translate_ru_eng('кот'))
print(translate_eng_ru('routing'))