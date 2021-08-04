list_numbers = [1, 2, 2, 3, 1, 1, 7, 7, 4, 4, 7, 4, 1, 1, 1, 1, 0, 5, 5, 5]


def plus(num):
    return num + 1


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
    step = 0
    new_list.append(0)
    for key in new_dict.keys():
        for num in new_list:
            if key == num:
                step += 1
                continue
            if new_dict.get(key) < step:
                new_dict[key] = step
                step = 0

    return new_dict


def main():
    value_dict = check_list(list_numbers)
    print(value_dict)


if __name__ == '__main__':
    main()
