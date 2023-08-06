import math

# Constants to represent players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    # Check rows, columns, and diagonals to find a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == PLAYER_X:
                return 10
            elif board[i][0] == PLAYER_O:
                return -10

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == PLAYER_X:
                return 10
            elif board[0][i] == PLAYER_O:
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER_X:
            return 10
        elif board[0][0] == PLAYER_O:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER_X:
            return 10
        elif board[0][2] == PLAYER_O:
            return -10

    return 0  # No winner

def is_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:  # Maximizer (AI) wins
        return score - depth

    if score == -10:  # Minimizer (human) wins
        return score + depth

    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best_score = max(best_score, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score

    else:  # Minimizing player (human)
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best_score = min(best_score, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    board[i][j] = EMPTY
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY

                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)

    return best_move

def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_full(board):
        # Human's turn
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    break
                else:
                    print("Cell already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")

        print_board(board)

        # Check if human wins
        if evaluate(board) == -10:
            print("Congratulations! You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # AI's turn
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X

        print("AI's move:")
        print_board(board)

        # Check if AI wins
        if evaluate(board) == 10:
            print("AI wins! Better luck next time!")
            break

    if not is_full(board) and evaluate(board) == 0:
        print("It's a draw!")

if __name__ == "__main__":
    main()
