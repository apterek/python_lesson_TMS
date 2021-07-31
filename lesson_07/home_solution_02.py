from tabulate import tabulate

# columns numbers in table
values_dict = {'customer': 0, 'product': 1, 'quantity': 2, 'cost': 3}


# creating a unique sequence of the column
def make_unique_list(filename, key):
    with open(filename, 'r') as file:
        return set([line.split()[0].split(',')[key] for line in file])


def make_table(filename, main_key, *args):
    args = args[0]  # change a tuple to a list
    # only for bd_internet_shop.txt, for other data tables need an empty dictionary
    table_dict = {'+': ['total sold: ', 'amount sold: ']}
    gen_dict = {}
    for column in make_unique_list(filename, main_key):
        # dictionary for save values of sum
        for i in range(len(args)):
            gen_dict[i] = 0
        # filling the dictionary
        for key, value in gen_dict.items():
            with open(filename, 'r') as file:
                for line in file:
                    # create iterable object from string
                    row = line.split()[0].split(',')
                    if row[main_key] == column:
                        # save sum in dictionary
                        gen_dict[key] = int(gen_dict[key]) + int(row[args[key]])
        # create dictionary with sum of columns
        table_dict[column] = [gen_dict.get(i) for i in range(len(args))]

    return table_dict


if __name__ == '__main__':
    print('Column name parameters that you can enter ({0}): '
          .format(', '.join([name
                             for name in values_dict.keys()])))
    filename_in = input('Enter file name: ')
    main_column = input('Enter column name with a value'
                        ' that is repeated more than once: ')
    column_for_sum = input('Enter the columns for which'
                           ' you want to get their sum separated by commas: ')
    headers_tabulate = [main_column]
    print(tabulate(make_table(filename_in, values_dict.get(main_column),
                              [values_dict.get(number_of_column)
                               for number_of_column in column_for_sum.split(',')]),
                   headers='keys', tablefmt='grid', stralign='center'))
