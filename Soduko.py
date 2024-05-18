import random

class Cell:
    def __init__(self, row, col, box, value=0):
        self.row = row
        self.col = col
        self.value = value
        self.box = box


class SudokuBoard:
    def __init__(self):
        self.board = None
        self.rows = {}
        self.columns = {}
        self.boxes = {}
        self.cells = []

    def create_board(self, rows, columns):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]  # columns and rows are set to 9
        self.rows = {i: set() for i in range(rows)}  # creating dictionary with sets of rows where i(the row) is the key and the index is the value
        self.columns = {i: set() for i in range(columns)} #same as above
        self.boxes = {i: set() for i in range(rows // 3 * columns // 3)} #same as above
        for row in range(rows):
            for col in range(columns):
                box_index = 3 * (row // 3) + (col // 3)
                cell = Cell(row, col, int(box_index))
                self.cells.append(cell)
                self.rows[row].add(cell)
                self.columns[col].add(cell)
                self.boxes[box_index].add(cell)

    def addToCellValueToBoard(self,value,row,col):
        self.board[row][col] = value

    def fill_board(self):
        if self.solve_board():
            # filling the board with solved values
            for cell in self.cells:
                self.addToCellValueToBoard(cell.value, cell.row, cell.col)
        else:
            print("Unable to solve the board.")

    def solve_board(self):
        for cell in self.cells:
            if cell.value == 0:
                for num in range(1, 10):
                    if self.is_valid(cell, num):
                        cell.value = num
                        if self.solve_board():
                            return True #if the whole board is filled
                        cell.value = 0
                return False
        return True



    def is_valid(self, cell, num):
        for currentCell in self.rows[cell.row]:
            if currentCell.value == num:
                return False
        for currentCell in self.columns[cell.col]:
            if currentCell.value == num:
                return False
        for currentCell in self.boxes[cell.box]:
            if currentCell.value == num:
                return False
        return True
    #checks if the current cells value not in the cells row,column,box


    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))  # prints each value in the row separated by a space


sudoku_board = SudokuBoard()
sudoku_board.create_board(9, 9)
sudoku_board.fill_board()
sudoku_board.print_board()

