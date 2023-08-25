print("aswini 192124096")
print("8 queen program")
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_queens(board, row, n):
    if row >= n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_queens(board, row + 1, n):
                return True
            board[row][col] = 0
    
    return False

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_queens(board, 0, n):
        print("No solution exists.")
    else:
        print_solution(board, n)

n = 6
solve_n_queens(n)
