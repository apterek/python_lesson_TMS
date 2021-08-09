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
    belka = 's t r e s s e d'
    belka_spisok = belka.split()
    belka_str = ''.join(belka_spisok[::-1])
    print(belka_str)


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
