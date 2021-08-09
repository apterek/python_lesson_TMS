def month_to_season(month_number):
    month_number = int(month_number)
    if month_number == 1 or month_number == 2 or month_number == 12:
        print('winter')
    elif month_number == 3 or month_number == 4 or month_number == 5:
        print('spring')
    elif month_number == 6 or month_number == 7 or month_number == 8:
        print('summer')
    elif month_number == 9 or month_number == 10 or month_number == 11:
        print('autumn')


month = input("Enter number of month from 1 to 12: ")
month_to_season(month)
