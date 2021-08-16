from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


def create_database_first() -> bool:
    DB_USER = "manti"
    DB_PASSWORD = "manti"
    DB_NAME = "manti"
    DB_ECHO = True

    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)
        return True
    return False
