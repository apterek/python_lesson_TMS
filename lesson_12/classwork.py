from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


def create_database_first() -> bool:
    DB_USER = "postgres"
    DB_PASSWORD = "271036yY#"
    DB_NAME = "NEW_DB"
    DB_ECHO = True
    DB_PORT = 54322

    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)
        return True
    return False

DB_USER = "danila"
DB_PASSWORD = "271036yY#"
DB_NAME = "pythondb"
DB_ECHO = True
DB_PORT = 54325


def create_connect_to_db():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}", echo=True
    )
    engine.connect()
    if not database_exists(engine.url):
        create_database(engine.url)
        return print('Database created')
    else:
        return print('Database already exist')


create_connect_to_db()
