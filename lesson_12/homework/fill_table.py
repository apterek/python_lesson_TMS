from fuction_to_work_with_db import add_product_table


def fill_product_table(session, filename: str):
    #  fill product table
    with open(filename) as file:
        for line in file:
            name, price = line.split(',')
            add_product_table(session, name, float(price))


