from solution_class_05 import numbers


def main():
    starts = int(input('Enter start number'))
    ends = int(input('enter last number'))
    if ends <= 1 or starts <= 0:
        print('Mistake, enter other numbers')
    numbers(starts, ends)


if __name__ == '__main__':
    main()
