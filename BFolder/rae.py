from curses import COLOR_RED, color_content
from turtle import color


board = []

print("Welcome to tic tac toe tea teh!")
print("Same as tic tac toe, but on a 5x5 grid.")
print("Match 4 first to win!")

for row in range(5):
    board.append([" ", " ", " ", " ", " "])   
     
turn = True
while True:
    row = input()
    column = input()
    if(int(row) >= 1 and int(row) <= 5):
        if(int(column) >= 1 and int(column) <= 5):
            if (turn):
                if (board[int(row) - 1][int(column) -1]!="0"):
                    if (board[int(row) - 1][int(column) -1]!="x"):
                        board[int(row) - 1][int(column) -1] = "0"
                        turn = not turn
                    else:
                        print("Already taken, take another turn")
                else:
                    print("Already taken, take another turn")
            else:
                if (board[int(row) - 1][int(column) -1] != "0"):
                    if(board[int(row) - 1][int(column) - 1] != "x"):
                        board[int(row) - 1][int(column) -1] = "x"
                        turn = not turn
                    else:
                        print("Already taken, take another turn")

                else:
                    print("Already taken, take another turn")
        
        else:
            print("Out of bounds, take another turn")
    else:
        print("Out of bounds, take another turn")


    for row in board:
        print(row)

