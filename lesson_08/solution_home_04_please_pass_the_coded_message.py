def hanoi_towers(n_2, start, finish, x):
    if n_2 == 1:
        return print(n_2, start, finish), print(x)
    else:
        tmp = 6 - start - finish
        hanoi_towers(n_2 - 1, start, tmp)
        print(n_2, start, finish)
        hanoi_towers(n_2 - 1, tmp, finish)



#n = int(input())
hanoi_towers(8, 1, 3)
