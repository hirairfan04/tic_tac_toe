import utils.check as check

def compturn(board):
    pos = -1
    value = -2
    for i in range (0,9):
        if (board[i] == 0):
            board[i] = 1
            score = -minmax(board , -1)
            board[i] = 0
            if (score>value):
                value = score
                pos = i
    board[pos] = 1


def minmax(board, player):
    x = check.analyzeboard(board)
    if(x != 0):
        return (x*player)
    pos = -1
    value = -2
    for i in range (0,9):
        if (board[i] == 0):
            board[i] = player
            score = -minmax(board , player*-1)
            board[i] = 0
            if (score>value):
                value = score
                pos = i
    if(pos == -1):
        return 0
    return value