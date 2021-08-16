import solution

commands_dict = {1: solution.create_table,
                 2: solution.read_table,
                 3: solution.update_table,
                 4: solution.add_data,
                 5: solution.delete_data}

template = """
Please choose one of the options:
1. Create table in database
2. Print table
3. Update row in table
4. Add row in table
5. Delete row from table
"""


def main():
    while True:
        options = int(input(template))
        command = commands_dict.get(options)
        database = 'product.db'
        if options == 1:
            print('Table already exist')
        elif options == 2:
            command(database)
        elif options == 3:
            print("Enter name, cost, quantity and comment, and row id by commas: ")
            name, cost, quantity, comment, id_name = input().split(',')
            command(database, name, float(cost), int(quantity), comment, int(id_name))
        elif options == 4:
            print("Enter name, cost, quantity and comment by commas: ")
            name, cost, quantity, comment = input().split(',')
            command(database, name, float(cost), int(quantity), comment)
        elif options == 5:
            print("Enter rows id for delete: ")
            rows_id = int(input())
            command(database, rows_id)
        else:
            return print("It's the end")


if __name__ == "__main__":
    main()
