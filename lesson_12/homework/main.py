from connection_module import create_connect_to_db
from models import User, Column, Product, Purchase


def main():
    session = create_connect_to_db('danila', '271036yY#', 'pythondb', 127.0.0.1, )
    pass


if __name__ == "__main__":
    main()