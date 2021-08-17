from models import Base, User, Product, Purchase
from sqlalchemy.orm import sessionmaker


def add_user_table(session, email_name: str):
    Session = sessionmaker(bind=session)
    session1 = Session()
    session1.add(User(email=email_name))
    session1.commit()


def add_product_table(session, product_name: str, product_cost: float):
    Session = sessionmaker(bind=session)
    session1 = Session()
    session1.add(Product(name=product_name, cost=product_cost))
    session1.commit()


def create_tables(session):
    Base.metadata.create_all(session)

