#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or\
                board[i] + 1 == col + row:
                    return False
    return True

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row):
        if row == N:
            print(board)
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1)

    solve([0] * N, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
