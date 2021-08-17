from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    email = Column(String(200), nullable=False)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost = Column(Float(), nullable=False)


class Purchase(Base):
    __tablename__ = 'Purchase'
    user_id = Column(Integer(), ForeignKey('users.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    quantity = Column(Integer(), nullable=False)
    date = Column(DateTime, default=datetime.utcnow())

