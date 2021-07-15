def exercise_1():

    x = 2 + (2 * (2 - 2)) / 2

    print(x)


def exercise_2():

    deposit = 2130
    deposit_time = 5
    annual_percent = 10
    bonus = 120

    for i in range(deposit_time):
        deposit = deposit + (deposit / annual_percent) + bonus
    
    print(deposit)


def exercise_3():
    belka = 'a s o u d h g u o a s h d g o s s'
    belka_spisok = belka.split()
    belka_str = ''.join(belka_spisok).upper()
    print(belka_str)


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
