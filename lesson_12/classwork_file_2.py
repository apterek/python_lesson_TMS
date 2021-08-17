import classwork


if __name__ == '__main__':
    result = classwork.create_database_first()
    if result:
        print('Database create !')
    else:
        print('Something going wrong')
