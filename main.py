#By Mharrech Ayoub
# Define the Sudoku puzzle grid where 0 represents an empty cell
Sudoku_table = [
    [5, 0, 0, 0, 2, 7, 0, 8, 9],
    [0, 0, 4, 0, 1, 0, 0, 0, 2],
    [0, 7, 2, 5, 9, 0, 3, 0, 0],
    [9, 0, 0, 4, 0, 0, 8, 0, 3],
    [0, 4, 7, 9, 0, 0, 0, 0, 0],
    [1, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 1, 7, 5, 2, 0, 0],
    [0, 0, 1, 0, 6, 0, 5, 0, 7],
    [0, 0, 5, 0, 4, 8, 0, 9, 1]
]

#PART 1 : the current state of the Sudoku grid 
def display_sudoku(Sudoku_table):

    # Display the Sudoku grid with clear formatting
    for i in range(len(Sudoku_table)):
        if i % 3 == 0 and i != 0:
            print("---------------------")  # Print row separator every three lines
          
        # Iterate over each cell in the current row to display its value
        for j in range(len(Sudoku_table[0])):
            # Add a vertical bar separator after every third cell, except before the first cell in a row
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  # Print column separator every three cells
            
            # Check if the current cell is the last in its row
            if j == 8:
                print(Sudoku_table[i][j])  # Print the last cell in the row and move to the next line
            else:
                print(str(Sudoku_table[i][j]) + " ", end="")  # Print cell value followed by a space

#Part 2 Checking
def find_empty_cell(Sudoku_table):

    # Search for an empty cell in the grid
    for i in range(len(Sudoku_table)):
        for j in range(len(Sudoku_table[0])):
            if Sudoku_table[i][j] == 0:
                return (i, j)  # Return the coordinates of the empty cell

    return None

#Part 3 Validation
def is_move_valid(Sudoku_table, num, position):
    # Check the row for the same number, excluding the current position
    for i in range(len(Sudoku_table[0])):
        if Sudoku_table[position[0]][i] == num and position[1] != i:
            return False  # Invalid move if the same number is found in the row

    # Check the column for the same number, excluding the current position
    for i in range(len(Sudoku_table)):
        if Sudoku_table[i][position[1]] == num and position[0] != i:
            return False  # Invalid move if the same number is found in the column

    # Identify the 3x3 subgrid that the position falls into
    box_x = position[1] // 3
    box_y = position[0] // 3
    
    # Check the subgrid for the same number, excluding the current position
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if Sudoku_table[i][j] == num and (i, j) != position:
                return False  # Invalid move if the same number is found in the 3x3 subgrid

    return True  # The move is valid if none of the above conditions are met



#Part 4 Solving
def solve_sudoku(Sudoku_table):
    
    # Find the first empty cell in the grid
    empty_position = find_empty_cell(Sudoku_table)
    # If no empty cell is found, it means the puzzle is solved
    if not empty_position:
        return True
    else:
        row, column = empty_position  # Unpack the position of the empty cell

    # Try all numbers from 1 to 9 in the empty cell
    for num in range(1, 10):
        # Check if the current number can be placed in the empty cell without violating Sudoku rules
        if is_move_valid(Sudoku_table, num, (row, column)):
            Sudoku_table[row][column] = num  # Temporarily place the number in the grid

            # Recursively try to solve the rest of the puzzle with this number in place
            if solve_sudoku(Sudoku_table):
                return True  # If successful, propagate the True result back up the recursion chain

            # If placing the current number doesn't lead to a solution, remove it and try the next number
            Sudoku_table[row][column] = 0  # This is the backtracking step

    # If no number from 1 to 9 leads to a solution in the current configuration, return False
    return False  # This triggers backtracking in the previous level of recursion

#Finally Printing 
#display_sudoku(Sudoku_table)
#solve_sudoku(Sudoku_table)
#print("___________________")
#display_sudoku(Sudoku_table)
