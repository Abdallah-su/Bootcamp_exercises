def display_board(board):
    print("\n")
    for  row in board :
        print("|".join(row))
        print ("-" * 9)
board=[[" "for _ in range(3)] for _ in range(3)]

def player_input(player, board):
    while True :
        try:
            row= int(input(f"player {player}, enter row (0-2)"))
            col =int(input(f"player {player}, enter col (0-2)"))
            if 0<=row<=2 and 0<=col<=2:
                if board [row][col]==" ":
                    return row, col
                else: print("the spot has already be taken")
            else: print("Invalid input! please  enter a valid number")
        except  ValueError:print(" enter a valid number (0-2)")
def check_win(board, player):
    for i in range(3):
        if all(board [i][j] ==player for j in range(3)): return True

        if all(board[i][i] == player for i in range(3) ) :return True
        if all(board[i][2-i]==player for i in range(3)): return True
        else: return False

def check_tie(board):
    return all(cell != " " for row in board for cell in row)   

def play():
    board = [[" " for _ in range(3)] for _ in  range(3)]  
    current_player ="X" 
    game_on = True
    while game_on:
        display_board(board)
        row, col = player_input(current_player, board)
        board[row][col]= current_player
        if check_win(board, current_player):
            display_board(board)
            print(f"player {current_player} wins") 
            game_on = False
        elif check_tie(board):
            display_board(board)
            print("it's a tie")
            game_on = False
        else:current_player ="O" if current_player ==   "X" else "X"
