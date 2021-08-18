from connection_module import create_connect_to_db
from fuction_to_work_with_db import create_tables, fill_purchase_table, user_purchases, add_user_table
from fill_table import fill_product_table
from sqlalchemy.orm import sessionmaker


template = """
Please choose one of the options:
1. Create tables in database(create database if database dosen't exist)
   Table create from file "models.py": 
2. Fill "product" table: 
3. Add user: 
4. Add transaction: 
5. Displaying all products purchased by a user: 
"""


# user interface program
def main():
    session = create_connect_to_db('danila', '271036yY#', 'pythondb', 'localhost', 54325)
    while True:
        print(template)
        parameter = int(input())
        if parameter == 1:
            create_tables(session)
            print("-" * 40, "\n", "-" * 13, "TABLES CREATED", "-" * 13, "\n", "-" * 40)
        elif parameter == 2:
            filename = input("Enter file name with parameter: produc,price:")
            fill_product_table(session, filename="product_infomation.csv")
            print("-" * 40, "\n", "-" * 13, "TABLES FILLED", "-" * 13, "\n", "-" * 40)
        elif parameter == 3:
            user_name = input("Enter email new user: ")
            Session = sessionmaker(bind=session)
            session1 = Session()
            add_user_table(session1, user_name)
            print("-" * 40, "\n", "-" * 13, "USER ADDED SUCCESSFULLY", "-" * 13, "\n", "-" * 40)
            session1.commit()
        elif parameter == 4:
            email = input("Enter user email: ")
            product = input("Enter product name: ")
            quantity = int(input("Enter quantity bought product: "))
            fill_purchase_table(session, email, product, quantity)
            print("-" * 40, "\n", "-" * 13, "TRANSACTION ADDED SUCCESSFULLY", "-" * 13, "\n", "-" * 40)
        elif parameter == 5:
            mail = input("Enter user email: ")
            print(f"User with email {mail} bought:")
            for prod in user_purchases(session, mail):
                print("---"*30,"\n", prod)
            print("---"*30)
        else:
            return print("It's the end, good day!")


if __name__ == "__main__":
    main()
