def test(last_number):  # Function find all divisor without a remainder
    result_1 = []  # Empty list
    for num in range(last_number + 1):  # take all the numbers up to the received
        if num == 0:  # if number = 0 miss
            continue
        if last_number % int(num) == 0:  # check if number divided on number without a remainder
            result_1.append(num)         # if yes, the number added to list
    return result_1  # return list


def check_len(numb_):
    if len(test(numb_)) == 2:                 # chek list length
        return result.append(test(numb_)[1])  # if list length = 2, add to final result


def numbers(start_number, end_number):
    if end_number == 1:  # it will work, if start_number = 1
        return result.append(1)
    if end_number == start_number:  # check when take last number
        check_len(end_number)
        return
    if check_len(end_number):  # checking is the number a prime
        pass
    end_number -= 1
    numbers(start_number, end_number)


def main():
    starts = int(input('Enter start number'))
    ends = int(input('enter last number'))
    if ends <= 1 or starts <= 0:
        print('Mistake, enter other numbers')
    numbers(starts, ends)
    print(result[::-1], '\n', 'length:', len(result))


if __name__ == '__main__':
    result = []
    main()
