#!/bin/python
class jasstr:
    def __init__(self, data):
        # data, array of bytes [0x22, 0x40, 0x60, ...]
        self.data = data

    def print(self):
        print("".join([chr(byte) for byte in self.data]))

    def is_lower(self):
        for byte in self.data:
            # Check if the byte is upper case, if it is
            # bail out and return False.
            if byte >= 65 and byte <= 90:
                return False
        return True

    def is_digit(self):
        for byte in self.data:
            if byte >= 0x30 and byte <= 0x39:
                continue
            return False
        return True

    # TODO- IMPLEMENT ADD

    def add(self, other):
        added_data = self.data + other.data
        return jasstr(added_data)

    # TODO- IMPLEMENT LEN

    def len(self):
        return len(self.data)


    # TODO- IMPLEMENT to_int
    #a typo 8bit signed is -127 to 127
'''
    def to_int(self):
        try:
            for num_int in self.data:
                if num_int >= -127 and num_int <= 127:
                    return int(''.join(map(chr, self.data))) #map is used to apply a given function to all the elements of an iterable(like a list).
        except ValueError:
            print("Error: The string contains non-digit characters.")
            return None

'''

#The right to_int function
def to_int(self):
    value = 0
    for byte in self.data:
        # Make sure the byte is a digit
        if byte < 0x31 or byte > 0x39:
            raise Exception("String has non-digit chars")
        digit_value = byte - 0x30;
        value = (value * 10) + digit_value
    return value

if __name__ == "__main__":
    a = jasstr([0x36, 0x31, 0x32, 0x33, 0x69, 0x41])
    b = jasstr([0x41, 0x32, 0x33, 0x34, 0x69, 0x40])
    a.print()
    print(a.is_lower())
    c = a.add(b)
    c.print()
    print(a.len())
    print(a.to_int())

'''
#TODO- class practice:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"The car's make: {self.make}, model: {self.model}, and year: {self.year}")
    def update_year(self, new_year):
        self.new_year = self.year
        return self.year


#inheritence
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def describe_battery(self):
        return f"Battery capacity: {self.battery_capacity}"


instance1 = Car("Toyota", "Camry", 2024)
print(instance1.display_info())

ElectricCarInstance = ElectricCar(input('what the car brand? '), input('what the modol? '), 2024, 30)
print(ElectricCarInstance.display_info())
print(ElectricCarInstance.describe_battery())
'''
'''


class User:
    def __init__(self, user_id,user_name):
        self.seats = user_id
        self.user_name = user_name
        self.followers = 7

user_1 = User('001', 'Jasmine')
user_2 = User('002', 'Nicole')

print(user_1.followers)

'''
'''
#TODO- list using classes
import colorsys
todo_list = []
class Todo_list:
    def __init__(self,user_input1, user_input2):
        user_input1 = input('add new task: ')
        user_input2 = input('do you wont to mark one of the tasks complete? (y/n)')

        self.user_input1 = user_input1
        self.user_input2 = user_input2

    def new_task(self):
        self.user_input1.append(todo_list)
    def complete_task(self):
        if self.user_input2 in todo_list:
            todo_list.remove(self.user_input2)
            print(self.user_input2.g) and print(todo_list)

print(Todo_list.__init__(input('add new task: '), input('do you want to mark one of the tasks complete? (y/n)')))

'''
'''

#practice_code

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

'''
'''
#More practice


class Elevator:
    def __init__(self, number_of_levels = 5 , current_floor = 3):
        self.number_of_levels = number_of_levels
        self.current_floor = current_floor
    def elevator_in_the_house(self):
        print(f'the number of floors in the house is: {self.number_of_levels}')
        print(f'the number of the current floor is: {self.current_floor}')


elevator1 = Elevator(6,5)
elevator2 = Elevator()

print(elevator1.elevator_in_the_house())

'''































































