from models import Base, User, Product, Purchase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


def add_user_table(session, email_name: str):
    Session = sessionmaker(bind=session)
    session1 = Session()
    session1.add(User(email=email_name))
    session1.commit()


def add_product_table(session, product_name: str, product_cost: float):
    Session = sessionmaker(bind=session)
    session1 = Session()
    session1.add(Product(name=product_name, price=product_cost))
    session1.commit()


def fill_purchase_table(session, *args: (str, str, int)):
    email_user, product_name, quntity_product = args
    Session = sessionmaker(bind=session)
    session1 = Session()

    email_require = select(User).where(User.email == email_user)
    if not session1.execute(email_require):
        add_user_table(session, email_user)
        id_user = [res.id for res in session1.execute(email_require).scalars()][0]
    else:
        id_user = [res.id for res in session1.execute(email_require).scalars()][0]

    product_require = select(Product).where(Product.name == product_name)
    if not session1.execute(product_require):
        return print('Something going wrong')
    else:
        id_product = [rest.id for rest in session1.execute(product_require).scalars()][0]
        price = [rest.id for rest in session1.execute(product_require).scalars()][2]
    total_cost = quntity_product * float(price)

    session1.add(Purchase(user_id=id_user, product_id=id_product, quntity=quntity_product, cost=total_cost))


def create_tables(session):
    Base.metadata.create_all(session)

