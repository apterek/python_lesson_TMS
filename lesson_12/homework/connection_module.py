from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


#  Created connetc to database
def create_connect_to_db(user: str, password: str, db_name: str, address_db: str, port_db: int):
    engine = create_engine(
        f"postgresql://{user}:{password}@{address_db}:{port_db}/{db_name}"
    )
    # check exists database
    if not database_exists(engine.url):
        # if database not exist created database with name (db_name)
        create_database(engine.url)
        print("Database create, continue... Connection secsfull!")
        return engine
    # if database exists, return what all OK!
    else:
        print("Connection secsfull!")
        return engine

