from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists


def create_connect_to_db(user: str, password: str, db_name: str, address_db: int, port_db: int):
    engine = create_engine(
        f"postgresql://{user}:{password}@{address_db}:{port_db}/{db_name}", echo=True
    )
    session = Session(bind=engine)
    if not database_exists(engine.url):
        create_database(engine.url)
        return session, print("Database create, continue... Connection secsfull!")
    else:
        return session, print("Connection secsfull!")

