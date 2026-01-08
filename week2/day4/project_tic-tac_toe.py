

# --- STEP 1: DISPLAY STATION ---
def display_board(board):
    print("\n")
    for i in range(len(board)):
        # Creates the vertical sticks
        print(" " + " | ".join(board[i]) + " ")
        # Creates the horizontal sticks between rows
        if i < 2:
            print("-----------")

# --- STEP 2: INPUT STATION ---
def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken!")
            else:
                print("Invalid range! Please pick 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# --- STEP 3: WINNER CHECKING STATION ---
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# --- STEP 4: TIE CHECKING STATION ---
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# --- STEP 5: THE MAIN GAME LOOP (THE BRAIN) ---
def play():
    # Step 1: Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_on = True
    
    while game_on:
        display_board(board)
        row, col = player_input(current_player, board)
        
        # Update the board data
        board[row][col] = current_player
        
        # Check if the game should end
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_on = False
        elif check_tie(board):
            display_board(board)
            print("It's a draw!")
            game_on = False
        else:
            # Switch player: If X, go to O. If O, go to X.
            current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play()