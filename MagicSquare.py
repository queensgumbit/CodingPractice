
#Magic square that generate odd numbers - odd_numXodd_num
class MagicSquare:
     def __init__(self):
         self.odd_num = None
         self.magic_sum = None
         self.square = None


     def odd_number(self):
         while True:
             try:
                 self.odd_num = int(input('Enter an odd number: '))
                 if self.odd_num % 2 != 0:
                     break
                 else:
                     print("Please enter an odd number.")
             except ValueError:
                 print("Invalid input. Please enter an integer.")



     def generate_magic_square(self):
         self.odd_number()
         self.magic_sum = self.odd_num * (self.odd_num ** 2 + 1) // 2 #using the formula
         self.square = [[0] * self.odd_num for _ in range(self.odd_num)] #use underscore ('_') to indicate that i do not need the value.
         num = 1
         r = 0
         c = self.odd_num // 2  #r=0 represents the row index where the algorithm starts  c=self.odd_num // 2 - represents the column index.

         while num <= self.odd_num ** 2:
             self.square[r][c] = num
             num += 1
             new_r, new_c = (r - 1) % self.odd_num, (c + 1) % self.odd_num #We move one row up ((r - 1)) and one column to the right ((c + 1)), the use of % help us wrap around the edges.
             if self.square[new_r][new_c]:
                 r += 1   #If the calculated position is already occupied by a number,move down one row without changing the column.
             else:
                 r, c = new_r, new_c #if the position is not occupied , we can move to this position.

        #the logic behind this : the algorithm ensures that no number is repeated in the same row or column,
        #and each cell contains a unique number from 1 to self.odd_num ** 2,
        #the sum of each row, column, and diagonal should be equal to self.magic_sum.

     def check_magic_square(self):
         # Checks rows
         for row in self.square:
             if sum(row) != self.magic_sum:
                 return False

         # Checks columns
         for column in range(self.odd_num):
             if sum(self.square[row][column] for row in range(self.odd_num)) != self.magic_sum:
                 return False

         # Checks diagonals
         diagonal_sum1 = sum(self.square[i][i] for i in range(self.odd_num)) #I use [i][i] because for instance for 3X3 MS: Diaganol looks like this: [1][1],[2][2],[3][3].
         diagonal_sum2 = sum(self.square[i][self.odd_num - 1- i] for i in range(self.odd_num)) #The opposite diaganol-for instance 3x3:[i = 0][3-1-i= 2],[1][1],[2][0]
         if diagonal_sum1 != self.magic_sum or diagonal_sum2 != self.magic_sum:
             return False

         return True

     def display_square(self):
         if self.check_magic_square():
             for row in self.square:
                 print(row)
         else:
             print("Magic square not generated yet.")

generate = MagicSquare()
generate.generate_magic_square()
generate.display_square()









































