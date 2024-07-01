def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def make_move(board, move, player):
    row, col = divmod(move, 3)
    if board[row][col] not in ['X', 'O']:
        board[row][col] = player
        return True
    else:
        print("Invalid move. The cell is already occupied.")
        return False

def tic_tac_toe():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'
    print_board(board)
    
    while True:
        move = get_player_move(current_player)
        if make_move(board, move, current_player):
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print("The game is a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
