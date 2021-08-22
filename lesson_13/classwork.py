from math import sqrt

solar_tape = int(input("Enter how much do you have solar tape"))


def squares_calculation(tape):
    result = []
    step = 1  # number of pieces
    while True:
        # Finding the greatest solar panel
        large_squares = int(sqrt(tape)) ** 2
        result.append(large_squares)
        print(f'{step} piece {large_squares}')
        step += 1
        tape = tape - large_squares
        # if the tape is less than four meters, we divide it into pieces of one meter each
        if tape < 4:
            for i in range(tape):
                result.append(int('1'))
                print(f'{step} piece 1')
                step += 1
            break
    return result


print(squares_calculation(solar_tape))