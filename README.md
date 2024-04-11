# PythonSudokuSolver
This Sudoku Solver is a Python-based application designed to automatically solve Sudoku puzzles. The solver uses a backtracking algorithm to fill in the blank spaces in a given Sudoku grid with the correct numbers according to Sudoku rules. 


About the main.py

Part 1 :  display_sudoku
    This function prints the current state of the Sudoku grid in a well-formatted manner.
    It is designed to make the grid easily readable by adding visual separators between
    each block of three rows and columns, reflecting the classic Sudoku layout.
    Args:
    Sudoku_table (list of lists): The 9x9 grid representing the Sudoku puzzle.
    
    
Part 2 :  find_empty_cell
    This function scans the entire Sudoku grid to find the first empty cell, which is 
    indicated by a '0'. This function is essential for determining the next cell to try
    inserting numbers during the solving process.
    Args:
    Sudoku_table (list of lists): The 9x9 grid representing the Sudoku puzzle.
    Returns:
    tuple: The row and column indices of the first empty cell found, or None if no empty cell is found.

Part 3 : is_move_valid
    Determines if placing a specific number (num) in a given position (row, column)
    within the Sudoku grid violates Sudoku rules. This includes checks for the number's
    presence in the same row, column, and the 3x3 subgrid that the position belongs to.
    Args:
    Sudoku_table (list of lists): The 9x9 grid representing the Sudoku puzzle.
    num (int): The number to be placed in the Sudoku grid.
    position (tuple): A tuple representing the (row, column) of the cell where `num` is to be placed.
    Returns:
    bool: True if the placement is valid according to Sudoku rules, False otherwise.

Part 4 : solve_sudoku
    Attempts to solve the Sudoku puzzle by recursively trying to fill all empty cells.
    It uses a backtracking algorithm, which means it makes a series of choices one at a time,
    and if any choice leads to a failure (an invalid Sudoku state), it backtracks to make a 
    different choice, continuing this process until the puzzle is solved or deemed unsolvable.
    Args:
    Sudoku_table (list of lists): The 9x9 grid representing the Sudoku puzzle, where empty cells are denoted by 0.
    Returns:
    bool: True if the puzzle is solved successfully, False if no solution is found.


