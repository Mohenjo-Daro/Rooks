board = []

for row in range(3):
    board.append([" ", " ", " "])   
     
turn = True
while True:
    row = input()
    column = input()
    if(int(row) >= 1 and int(row) <= 3):
        if(int(column) >= 1 and int(column) <= 3):
            if (turn):
                board[int(row) - 1][int(column) -1] = "0"
                turn = not turn
            else:
                board[int(row) - 1][int(column) - 1] = "x"
                turn = not turn
        
        else:
            print("Error, take another turn")
    else:
        print("Error, take another turn")


    for row in board:
        print(row)

