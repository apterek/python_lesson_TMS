def function_3(*args, func_type):
    if func_type == 'min':
        return func_min(args)
    elif func_type == 'max':
        return func_max(args)


def func_min(min_input):
    min_element = min_input[0]
    for min_num in min_input:
        if min_num < min_element:
            min_element = min_num
    return min_element


def func_max(max_input):
    max_element = max_input[0]
    for max_num in max_input:
        if max_num > max_element:
            max_element = max_num
    return max_element


type_max_or_min = input("Enter max or min :")
print(function_3(-1, 5, 10, 33, -10, func_type=type_max_or_min))
