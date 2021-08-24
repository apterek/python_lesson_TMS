# ----------------------------------------------------------------
# This file declares which tables will be created in the database
# ----------------------------------------------------------------

from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    email = Column(String(200))

    purchase_user = relationship("Purchase", back_populates="users")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer(), primary_key=True)
    name = Column(String(200))
    price = Column(Float(32))

    purchase_product = relationship("Purchase", back_populates="products")


class Purchase(Base):
    __tablename__ = 'purchase'
    id = Column(Integer(), primary_key=True)

    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    users = relationship("User", back_populates="purchase_user")

    product_id = Column(Integer(), ForeignKey('products.id'), nullable=False)
    products = relationship("Product", back_populates="purchase_product")

    quantity = Column(Integer(), nullable=False)
    cost = Column(Float(), nullable=False)
    date = Column(DateTime, default=datetime.utcnow())

