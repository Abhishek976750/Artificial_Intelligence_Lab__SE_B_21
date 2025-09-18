import math

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check if moves are still left
def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

# Evaluate the board state
def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return +1
        elif row.count("O") == 3:
            return -1

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return +1
        elif board[0][col] == board[1][col] == board[2][col] == "O":
            return -1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return +1
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return -1
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return +1
    if board[0][2] == board[1][1] == board[2][0] == "O":
        return -1

    return 0  # Draw / not terminal yet

# Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If game over
    if score == 1:
        return score
    if score == -1:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:  # Maximizer's move
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = "_"
        return best
    else:  # Minimizer's move
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = "_"
        return best

# Find the best move for X
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# ----------------- Run the game -----------------
if __name__ == "__main__":
    board = [
        ["_", "X", "X"],
        ["O", "_", "_"],
        ["_", "_", "X"]
    ]

    print("Current board:")
    print_board(board)

    best_move = find_best_move(board)
    print("The best move for X is:", best_move)

