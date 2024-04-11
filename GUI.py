#By M.Ayoub

# Importing tkinter for GUI creation
from tkinter import Tk, Canvas, Entry, Button, Label, messagebox

# Define the initial Sudoku puzzle grid
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

# Utility functions from the non-GUI version adapted for GUI usage
def find_empty_cell(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                return (i, j)
    return None

def is_move_valid(table, num, position):
    for i in range(len(table[0])):
        if table[position[0]][i] == num and position[1] != i:
            return False

    for i in range(len(table)):
        if table[i][position[1]] == num and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if table[i][j] == num and (i, j) != position:
                return False

    return True

def solve_sudoku(table):
    find = find_empty_cell(table)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_move_valid(table, i, (row, col)):
            table[row][col] = i

            if solve_sudoku(table):
                return True

            table[row][col] = 0

    return False

# GUI Specific Functions
def setup_gui():
    window = Tk()
    window.title("Sudoku Solver")
    entries = []

    for i in range(9):
        row_entries = []
        for j in range(9):
            e = Entry(window, width=5, font=('Helvetica', 18), justify='center', borderwidth=2)
            e.grid(row=i, column=j)
            if Sudoku_table[i][j] != 0:
                e.insert(0, Sudoku_table[i][j])
                e.config(state='readonly')
            row_entries.append(e)
        entries.append(row_entries)

    return window, entries

def solve_sudoku_gui(entries):
    table = [[int(entries[i][j].get() or 0) for j in range(9)] for i in range(9)]
    if solve_sudoku(table):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, "end")
                entries[i][j].insert(0, table[i][j])
                if Sudoku_table[i][j] == 0:
                    entries[i][j].config(fg='blue')
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists!")

def clear_sudoku_gui(entries):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, "end")
            if Sudoku_table[i][j] != 0:
                entries[i][j].insert(0, Sudoku_table[i][j])
            else:
                entries[i][j].config(fg='black')

def add_buttons(window, entries):
    solve_button = Button(window, text='Solve', command=lambda: solve_sudoku_gui(entries))
    solve_button.grid(row=9, column=1, columnspan=2, pady=10)

    clear_button = Button(window, text='Clear', command=lambda: clear_sudoku_gui(entries))
    clear_button.grid(row=9, column=4, columnspan=2, pady=10)

def run_gui():
    window, entries = setup_gui()
    add_buttons(window, entries)
    window.mainloop()

run_gui()
