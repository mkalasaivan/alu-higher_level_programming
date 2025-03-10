#!/usr/bin/python3
"""
N Queens Problem Solver
This script finds all possible solutions for placing N non-attacking queens on an NxN chessboard.
"""

import sys

def print_solutions(solutions):
    """Prints each solution in the required format."""
    for solution in solutions:
        print(solution)

def is_valid(board, row, col):
    """Check if placing a queen at board[row][col] is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """Finds all solutions for the N queens puzzle."""
    def backtrack(row, solution):
        if row == N:
            solutions.append([[i, solution[i]] for i in range(N)])
            return
        for col in range(N):
            if is_valid(solution, row, col):
                solution[row] = col
                backtrack(row + 1, solution)
                solution[row] = -1

    solutions = []
    backtrack(0, [-1] * N)
    return solutions

def main():
    """Main function to handle input and invoke the solver."""
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
    print_solutions(solutions)

if __name__ == "__main__":
    main()
