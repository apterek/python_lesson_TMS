# create chessboard
chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]


def move(x, y, z, t):
    answer = ''
    # placed the second queen on the board
    chessboard[z][t] = 2
    step = 7
    # finding for whether the first queen can beat the second
    for i in range(7):
        # finding queen by horizontal,verticals,diagonals from left to right from up to down,
        # diagonals from right to left from down to up
        if chessboard[x][i] == 2 or chessboard[i][y] == 2 or chessboard[i][i] == 2\
                or chessboard[i][i] == 2 or chessboard[i][step] == 2:
            answer = 'YES'
            break
        step -= 1
    if answer == 'YES':
        return answer
    else:
        return 'NO'


if __name__ == '__main__':
    position = input('Enter queen positions'
                     '(int the format x,y,z,t in range from 0 to 7): ')\
        .split(',')
    line_1, column_1, line_2, column_2 = position
    print(move(int(column_1), int(line_1), int(line_2), int(column_2)))


