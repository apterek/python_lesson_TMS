list_numbers = [1, 2, 2, 3, 1, 1, 7, 7, 4, 4, 4, 0, 5, 5, 5]


def plus(num):
    return num + 1


def check_list(lists):
    new_list = []
    for number in lists:
        if number == 0:
            break
        else:
            new_list.append(number)
    new_list.append(0)
    new_dict = {
        new: 0 for new in set(new_list)
    }
    step = 0
    print(new_list)
    for key in new_dict.keys():
        print(key)
        for num in new_list:
            if key == num:
                step += 1
                continue
            print('-', step)
            if new_dict.get(key) < step:
                new_dict[key] = step
                step = 0
    #new_ = sorted(new_dict, key=lambda x: new_dict.get(x))
    return new_dict


def main():
    value_dict = check_list(list_numbers)
    print(value_dict)
    #print(list_max_value[-1], 'met in the line:', value_dict.get(list_max_value[-1]), 'times')


if __name__ == '__main__':
    main()
