def numbers(start_number, end_number):
    while True:
        if end_number % end_number == 0 and end_number >= 1:
            if end_number == 1:
                return print(1)
            print(end_number)
            break
        else:
           end_number -= 1
    numbers (start_numbera, end_numbers)


if __name__ == '__main__':
    number(0, 100)
