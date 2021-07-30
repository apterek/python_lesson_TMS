student_list = [10, 13, 455]


def my_decorator(func):
    def add_one_desk(res):
        return func(res) + 1
    return add_one_desk


def calculation_number_of_desks(values):
    return int(values / 2)


numbers_of_desk = my_decorator(calculation_number_of_desks)
for index, value in enumerate(student_list):
    if value % 2 == 0:
        print(f'For {index + 1} class need - {int(calculation_number_of_desks(value))} desk')
    else:
        print(f'For {index + 1} class need - {numbers_of_desk(value)} desk')
