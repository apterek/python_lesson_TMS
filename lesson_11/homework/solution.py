import sqlite3


def create_table(table_name):
    # create connection with database and return an object representing it, and create file database product.db
    with sqlite3.connect('product.db') as session:
        cursor = session.cursor()  # create object cursor, which allows to make SQL queries to database
        pass
