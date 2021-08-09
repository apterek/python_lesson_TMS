def function_2(*args):
    per = args[0]
    sum_numbers = 0
    for number in args:
        sum_numbers += number
        if number > per:
            per = number
    return sum_numbers, per


print(function_2(1, 3, 5, 7, 11, 123, 322, 12))
