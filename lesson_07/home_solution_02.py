def read_file(filename):
    with open(filename) as file:
        for line in file:
            print(line.split(), '---' * 40)


read_file('bd_internet_shop.txt')