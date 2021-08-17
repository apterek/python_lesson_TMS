from connection_module import create_connect_to_db
from fuction_to_work_with_db import create_tables, fill_purchase_table
from fill_table import fill_product_table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models import Base, User, Product, Purchase


def fill_data(session):
    # create table by file modules.py
    create_tables(session)
    # fill table product
    fill_product_table(session, "product_infomation.csv")
    pass


def main():
    session = create_connect_to_db('danila', '271036yY#', 'pythondb', 'localhost', 54322)
    #output = ['vasya@mail.ru', 'switch', 5]
    fill_purchase_table(session, 'vasya@mail.ru', 'switch', 5)


if __name__ == "__main__":
    main()
