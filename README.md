# PythonSudokuSolver - Tkinter (GUI)
This Sudoku Solver is a Python-based application designed to automatically solve Sudoku puzzles. The solver uses a backtracking algorithm to fill in the blank spaces in a given Sudoku grid with the correct numbers according to Sudoku rules. 

<h2>Sudoku Solver Project</h2>

This repository hosts a Python-based project designed to solve Sudoku puzzles. It features both a command-line interface version (main.py) and a graphical user interface version (GUI.py), offering a versatile approach to tackling Sudoku puzzles programmatically.


<h2>About the main.py</h2>

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


<h2>Features</h2>

Command-Line Interface (CLI): main.py allows users to solve Sudoku puzzles in a text-based format, displaying the initial grid, processing the puzzle, and then outputting the solved grid.
Graphical User Interface (GUI): GUI.py offers a more interactive experience, where users can input numbers into a Sudoku grid, solve the puzzle with the click of a button, and clear the puzzle to start over. The GUI is built using the Tkinter library, making it easy to use for both beginners and experienced users alike.


<h2>How It Works</h2>

Initialization: For both versions, the Sudoku grid is initialized with a set of predefined numbers, where 0 represents an empty cell.
Solving Process:
CLI Version: Running main.py will automatically solve the predefined puzzle and display the solution in the terminal.
GUI Version: Upon launching GUI.py, users can manually enter numbers into the grid or use the predefined puzzle. Clicking the "Solve" button solves the puzzle, and the "Clear" button resets it.

<h2>Requirements</h2>

Python 3.x
Tkinter library for the GUI version (GUI.py)

<h2>Running the Project</h2>

For the CLI version, run python main.py in your terminal.
For the GUI version, run python GUI.py. This opens a window where you can interact with the Sudoku solver.

<h2>Contributions</h2>

Contributions to this project are welcome. Whether it's adding new features, improving the algorithms, or fixing bugs, feel free to fork the repository and submit a pull request.

<h2>License</h2>

Mharrech Ayoub
