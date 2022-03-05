board = []

for row in range(3):
    board.append([" ", " ", " "])   
     
turn = True
while True:
    row = input()
    column = input()
    if(turn):
        board[int(row) - 1][int(column) -1] = "0"
    else:
        board[int(row) - 1][int(column) - 1] = "x"

    turn = not turn


    for row in board:
        print(row)

