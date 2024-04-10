'''class Rectangle:
    def __init__(self,side1 = 10, side2 = 5):
        self.side1 = side1
        self.side2 = side2
    def calculated_area(self):
        Area = self.side1 * self.side2
        return Area

    def draw(self):
        line = '*' * self.side1
        number_of_lines = self.side2
        for i in range(number_of_lines):
            print(line)
r1 = Rectangle()
r1.draw()
'''

class Elevator:
    def __init__(self,number_of_floors = 5, current_floor = 3):
        self.number_of_floors = number_of_floors
        self.current_floor = current_floor
    def up(self):
        if self.current_floor == self.number_of_floors:
            return 'Elevator is not able to move higher'
        else:
            self.current_floor +=1
            return f'Elevator is moving on the {self.current_floor}th floor'

    def down(self):
        if self.current_floor == 1:
            return 'Elevator is not able to move lower'
        else:
            self.current_floor -= 1
            return f'Elevator is moving on the {self.current_floor}th floor'

E1 = Elevator(7,3)
print(E1.up())