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

Part 3 : 
