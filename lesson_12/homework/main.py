from connection_module import create_connect_to_db
from fuction_to_work_with_db import create_tables, add_user_table, add_product_table


def main():
    session = create_connect_to_db('danila', '271036yY#', 'pythondb', 'localhost', 54322)
    create_tables(session)
    add_user_table(session, 'vasya@mail.ru')
    add_product_table(session, 'switch', 1020.20)


if __name__ == "__main__":
    main()
