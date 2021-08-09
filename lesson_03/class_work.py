from math import sqrt


def exercise_3_4():
    dima = 25
    nikita = 22
    sergey = 52
    print((dima + sergey + nikita) / 3)


def exersice_5():
    side_square = 10

    parametr_square = list()

    parametr_square.append(4*side_square)
    parametr_square.append(side_square * side_square)
    parametr_square.append(sqrt(2) * side_square)

    print(parametr_square)


def exersice_6():
    my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
    my_list_2 = set(my_list)
    print(len(my_list) - len(my_list_2))


def exersice_7():
    my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
    print(my_list[1:4])


if __name__ == "__main__":
    exercise_3_4()
    exersice_5()
    exersice_6()
    exersice_7()
