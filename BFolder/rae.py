board = []

print("Welcome to tic tac toe tea teh!")
print("Same as tic tac toe, but on a 5x5 grid.")
print("Match 5 first to win!")

for row in range(5):
    board.append([" ", " ", " ", " ", " "])   
     
turn = True
gameOver = False

def check(board):
    #rows
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4]):
        gameOver = True
    #if (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4]):
    #    print("END")
    #if (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4]):
    #    print("END")
    #if (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4]):
    #    print("END")
    #if (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4]):
    #    print("END")

    #columns
    #if (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0]):
    #    print("END")
    #if (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1]):
    #    print("END")
    #if (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2]):
    #    print("END")
    #if (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3]):
    #    print("END")
    #if (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4]):
    #    print("END")

    #diagonals
    #if (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4]):
    #    print("END")
    #if (board[0][4] == board[1][3] and board[0][4] == board[2][2] and board[0][4] == board[3][1] and board[0][4] == board[4][0]):
    #    print("END")
    
    

while not gameOver:
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
    
    check(board)
