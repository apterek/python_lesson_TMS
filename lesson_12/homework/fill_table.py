from fuction_to_work_with_db import add_product_table


# Filling the table product from a file
def fill_product_table(session, filename: str):
    with open(filename) as file:
        for line in file:
            name, price = line.split(',')
            add_product_table(session, name, float(price))


