from typing import List

from models import Base, User, Product, Purchase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


# Decorator for create permanent connection
def decorarator_session(func):
    def connect(session, *args):
        Session = sessionmaker(bind=session)
        session1 = Session()
        result = func(session1, args)
        session1.commit()
        return result
    return connect


# Add user to the table with name "user"
def add_user_table(session, *args: str):
    email_name = str(args[0])
    session.add(User(email=email_name))


# Add product with price in the table "product"
@decorarator_session
def add_product_table(session, *args: (str, float)):
    product_name, product_cost = args[0]
    session.add(Product(name=product_name, price=product_cost))


# find id by email in the table "user", if user email not exists, added email in table
def take_user_id(session, *args: str):
    user_email = args[0]
    email_require = select(User).where(User.email == user_email)
    if not [res.id for res in session.execute(email_require).scalars()]:
        add_user_table(session, user_email)
        id_user = [res.id for res in session.execute(email_require).scalars()][0]
    else:
        id_user = [res.id for res in session.execute(email_require).scalars()][0]
    return id_user


# Add transaction in the table "Purchase", request id email user in the table "users",
# adding it in a column "user_id", request product id in the table "product",
# adding it in a column "product_id", in quantity column added parameter "quntity_product",
# in cost column added total amount of all purchase, date added time from funcion "datetime.utcnow()"
@decorarator_session
def fill_purchase_table(session, *args: (str, str, int)):
    email_user, product_name, quntity_product = args[0]
    id_user = take_user_id(session, email_user)
    product_require = select(Product).where(Product.name == product_name)
    if not session.execute(product_require):
        return print('Something going wrong')
    else:
        id_product = [rest.id for rest in session.execute(product_require).scalars()][0]
        price = [rest.price for rest in session.execute(product_require).scalars()][0]
    total_cost = quntity_product * float(price)
    session.add(Purchase(user_id=id_user, product_id=id_product, quantity=quntity_product, cost=total_cost))
    return print('Data is added')


# Finding email id in table users , and print all transaction with this id
@decorarator_session
def user_purchases(session, user_email):
    id_user = take_user_id(session, user_email)
    user_require = select(Purchase).where(Purchase.user_id == id_user)
    product_id = [res.product_id for res in session.execute(user_require).scalars()]
    product_list = []
    for id_p in product_id:
        product_require = select(Product).where(Product.id == id_p)
        name_product = str([rest.name for rest in session.execute(product_require).scalars()][0])
        product_list.append(name_product)
    return product_list


# Created table from file "models.py"
def create_tables(session):
    Base.metadata.create_all(session)
<<<<<<< HEAD
=======


def get_user_purchases(user: User) -> List[Purchase]:
    return user.purchase_user
>>>>>>> origin/main
