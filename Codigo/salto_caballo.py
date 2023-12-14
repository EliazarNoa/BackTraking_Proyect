def is_valid_move(x, y, board):
    if x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] == -1:
        return True
    return False

def solve_knight_tour(board, x, y, move_x, move_y, move_count):
    if move_count == len(board) * len(board):
        return True
    for i in range(len(move_x)):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if solve_knight_tour(board, next_x, next_y, move_x, move_y, move_count + 1):
                return True
            board[next_x][next_y] = -1
    return False

def print_board(board):
    for row in board:
        print(row)

def solve_knight_tour_problem():
    n = 8
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if solve_knight_tour(board, 0, 0, move_x, move_y, 1):
        print_board(board)
    else:
        print("No solution exists")

solve_knight_tour_problem()