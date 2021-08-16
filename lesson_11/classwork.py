from __future__ import division

import sqlite3
import _datetime


def create_user_table():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR,
            lastname VARCHAR,
            email VARCHAR,
            password VARCHAR,
            age INTEGER,
            datetime DATETIME
);
            """
        )
        session.commit()


def create_user(firstname: str, lastname: str, email: str, password: str, age: int, create_at):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
           INSERT INTO user (firstname, lastname, email, password, age, datetime)
           VALUES (?, ?, ?, ?, ?, ?);
           """,
            (firstname, lastname, email, password, age, create_at)
        )
        session.commit()


create_user_table()

create_user('Dima', 'Petrovich', 'asdf@mail.ru', '2tq4wef1', 23, _datetime.datetime.now())
create_user('Masha', 'Losa', 'sdfg@mail.ru', '3aw46ywg', 44, _datetime.datetime.now())
create_user('Kat9', 'Kiloa', 'hgfjghf@mail.ru', 'sye53w4q34', 33, _datetime.datetime.now())
create_user('Tima', 'Jasos', 'rudhdf@mail.ru', ' wq44w5', 61, _datetime.datetime.now())

