def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_player_move(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                return row, col
        print("Invalid move. Please try again.")

def tic_tac_toe():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'
    print_board(board)
    
    while True:
        row, col = get_player_move(current_player)
        board[row][col] = current_player
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
