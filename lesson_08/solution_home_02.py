list_numbers = [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5]


def check_list(lists):
    new_list = []
    for number in lists:
        if number == 0:
            break
        else:
            new_list.append(number)
    new_dict = {
        new: 0 for new in set(new_list)
    }
    for key in new_dict.keys():
        for num in new_list:
            if key == num:
                new_dict[key] = int(new_dict.get(key)) + 1
    new_ = sorted(new_dict, key=lambda x: new_dict.get(x))
    return new_, new_dict


def main():
    list_max_value, value_dict = check_list(list_numbers)
    print(list_max_value[-1], 'met in the line:', value_dict.get(list_max_value[-1]), 'times')


if __name__ == '__main__':
    main()
