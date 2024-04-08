#!/usr/bin/python3


import sys

class NQueensSolver:
    """
    Class to solve the N queens problem.

    Attributes:
        N (int): The size of the chessboard.
        board (list): 2D list representing the chessboard.
        solutions (list): List to store all solutions found.
    """
    def __init__(self, N):
        """
        Initializes the NQueensSolver object.

        Args:
            N (int): The size of the chessboard.
        """
        try:
            self.N = int(N)
        except ValueError:
            print("N must be a number")
            sys.exit(1)
        
        if self.N < 4:
            print("N must be at least 4")
            sys.exit(1)
        
        self.board = [['.' for _ in range(self.N)] for _ in range(self.N)]
        self.solutions = []

    def is_safe(self, row, col):
        """
        Checks if it is safe to place a queen at a given position.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it is safe to place a queen, False otherwise.
        """
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if self.board[i][j] == 'Q':
                return False
        
        return True

    def solve_nqueens(self, row):
        """
        Solves the N queens problem using backtracking.

        Args:
            row (int): The current row being processed.
        """
        if row == self.N:
            self.solutions.append(["".join(row) for row in self.board])
            return
        
        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.solve_nqueens(row + 1)
                self.board[row][col] = '.'

    def get_solutions(self):
        """
        Gets all solutions found for the N queens problem.

        Returns:
            list: List of all solutions found.
        """
        self.solve_nqueens(0)
        return self.solutions

def nqueens(N):
    """
    Solves the N queens problem and prints the solutions.

    Args:
        N (str): The size of the chessboard.

    Raises:
        ValueError: If N is not a valid integer.
    """
    solver = NQueensSolver(N)
    solutions = solver.get_solutions()
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        nqueens(sys.argv[1])
