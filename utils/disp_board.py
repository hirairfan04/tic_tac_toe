def constboard(board):
    print("Current state of the board: \n\n")

    for i in range (0,9):
        if((i>0) and (i%3 == 0)):
            print("\n")
        if(board[i] == 0):
            print("_ ", end = " ")
        elif(board[i] == 1):
            print("X ", end = " ")
        elif(board[i] == -1):
            print("O ", end = " ")
    print("\n\n")