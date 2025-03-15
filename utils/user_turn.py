def user1turn(board):
    pos = int(input("Enter X's position: "))
    if (board[pos-1] != 0):
        print("Wrong move....")
        exit(0)
    else:
        board[pos-1] = 1


def user2turn(board):
    pos = int(input("Enter O's position: "))
    if (board[pos-1] != 0):
        print("Wrong move....")
        exit(0)
    else:
        board[pos-1] = -1