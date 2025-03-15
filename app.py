from utils import user_turn
from utils import com_turn
from utils import check
from utils import disp_board as disp
   

def main():
    choice = int(input("Enter 1 for single player or 2 for multi-player: "))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if choice == 1:
        print("Computer: X Vs. You: O")
        player = int(input("Enter to play 1(st) or 2(nd): "))
        for i in range (0,9):
            if(check.analyzeboard(board) != 0):
                break
            if((i+player) % 2 == 0):
                com_turn.compturn(board)
            else:
                disp.constboard(board)
                user_turn.user2turn(board)
    else:
        for i in range (0,9):
            if(check.analyzeboard(board) != 0):
                break
            if(i%2 == 0):
                disp.constboard(board)
                user_turn.user1turn(board)
            else:
                disp.constboard(board)
                user_turn.user2turn(board)

    x = check.analyzeboard(board)

    if(x == 0):
        disp.constboard(board)
        print("Draw!")
    elif(x == -1):
       disp.constboard(board)
       print("Player O has won!")
    elif(x == 1):
        disp.constboard(board)
        print("Player X has won!") 

main()