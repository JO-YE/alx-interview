#!/usr/bin/python3
'''A Python program that solves the N Queens problem for a given N.'''

import sys


def is_queen_conflict(board, row, col, N):
    """
    Check if placing a queen at the given position conflicts
    with existing queens.

    Args:
        board (list): The current placement of queens on the board.
        row (int): The row to check for conflicts.
        col (int): The column to check for conflicts.
        N (int): The size of the board.

    Returns:
        bool: True if the position conflicts with existing queens,
        False otherwise.
    """
    # Check if there's a queen in the same row or diagonal
    for i in range(col):
        if board[row][i] == 1 or board[row][col - i - 1] == 1:
            return False
        if row - i - 1 >= 0 and board[row - i - 1][col - i - 1] == 1:
            return False
        if row + i + 1 < N and board[row + i + 1][col - i - 1] == 1:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and return a list of all solutions.
    Each solution is represented as a 2D list.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(row):
        """
        Recursively find solutions by placing queens row by row.
        """
        if row == N:
            solutions.append([_[:] for _ in board])
            return

        for col in range(N):
            if not is_queen_conflict(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions


if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])
