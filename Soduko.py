import random


#TODO- soduko game !!
# 9 squares - in each numbers from 1-9,in each row and column numbers from 1-9 just once
# the starting position should be with 32 already known numbers.


class Sudoku:
    def __init__(self):
        self.board = None
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def create_board(self, rows, columns):
        self.board = [[0] * columns for _ in range(rows)]
        self.fill_board()

    def fill_board(self):
        for i in range(9):
            for j in range(9):
                num = random.choice(self.numbers)
                while not self.is_valid(i, j, num):
                    random.shuffle(self.numbers)
                    num = random.choice(self.numbers)
                self.board[i][j] = num

    def is_valid(self, row, col, num):
        # Checks if the number is not in the current row
        if num in self.board[row]:
            return False

        # Checks if the number is not in the current column
        if num in [self.board[i][col] for i in range(9)]:
            return False

        # Checks if the number is not in the current 3x3 square
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True


sudoku_board = Sudoku()
sudoku_board.create_board(9, 9)

# Print the Sudoku board
for row in sudoku_board.board:
    print(row)
