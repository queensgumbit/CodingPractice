class Rectangle:
    def __init__(self, side_lenght, height):
        self.side_lenght = side_lenght
        self.height = height

    def calculated_area(self):

        area = int(self.side_lenght) * int(self.height)
        print(f'the calculated area of the rectangle is {area}')


side_length = input('Enter the side length of the rectangle: ')
height = input('Enter the height of the rectangle: ')

r1 = Rectangle(side_length, height)
r2 = Rectangle(side_length, height)

print(r1.calculated_area())
