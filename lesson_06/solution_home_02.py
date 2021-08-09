student_list = ["10", 13, "455"]


# apply decorator if number odd
def my_decorator(func):
    def add_one_desk(res):
        return func(res) + 1
    return add_one_desk


# dividing the number of students by 2
def calculation_number_of_desks(values):
    return int(int(values) / 2)


# advertise decorator
numbers_of_desk = my_decorator(calculation_number_of_desks)
for index, value in enumerate(student_list):
    # Parity definition numbers of student
    if int(value) % 2 == 0:
        print(f'For {index + 1} class need - {calculation_number_of_desks(value)} desk')
    else:
        print(f'For {index + 1} class need - {numbers_of_desk(value)} desk')
