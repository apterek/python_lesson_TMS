def print_result(result_dict):
    result_dict_1 = sorted(result_dict, key=lambda x: result_dict.get(x), reverse=True)

    for key, value in result_dict.items():
        print(f'{key} scored {value} point')

