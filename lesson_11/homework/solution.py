import sqlite3
from tabulate import tabulate


def create_table(database_name: str):
    # create connection with database and return an object representing it, and create file database product.db
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()  # create object cursor, which allows to make SQL queries to database
        cursor.execute(  # make sql request
            """
            CREATE TABLE product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            cost FLOAT,
            quantity INTEGER,
            comment TEXT
            
            );
            """
        )
        session.commit()  # close session


def read_table(name_database: str):
    with sqlite3.connect(name_database) as session:
        cursor = session.cursor()
        table = cursor.execute(
            """
            SELECT * FROM product;
            """
        )
        result = [result for result in table.fetchall()]
        print(tabulate(result))
        session.commit()


def update_table(nickname_database: str, *args: (str, float, int, str, int)):
    with sqlite3.connect(nickname_database) as session:
        cursor = session.cursor()
        cursor.execute("""
            UPDATE product SET name = ?, cost = ?, quantity = ?, comment = ? where id = ?;
            """, args)
        session.commit()


def add_data(database_nickname: str, *args: (str, float, int, str)):
    with sqlite3.connect(database_nickname) as session:
        cursor = session.cursor()
        cursor.execute("""
            INSERT INTO product (name, cost, quantity, comment)
            VALUES (?, ?, ?, ?);
            """, args)
        session.commit()


def delete_data(database, *args: int):
    with sqlite3.connect(database) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product WHERE id = ?;
            """, args)
        session.commit()


if __name__ == "__main__":
    pass
    # For test
    # add_data('product.db', 'cat', 132.32, 12, 'cats')
    # update_table('product.db', 'dog', 125.31, 15, 'dogs', 4)
    # read_table('product.db')
    # delete_data('product.db', 3)
    # read_table('product.db')
