def numbers(end_number):
    while True:
        if end_number % end_number == 0 and end_number >= 1:
            if end_number == 1:
                return print(1)
            print(end_number)
            end_number -= 1
            break
        else:
           end_number -= 1
    numbers (end_number)


if __name__ == '__main__':
    numbers(100)
