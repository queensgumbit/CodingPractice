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

    def addx(self, other):
        added_data = self.data + other.data
        return jasstr(added_data)

    # TODO- IMPLEMENT LEN

    def len(self):
        return len(self.data)


    # TODO- IMPLEMENT to_int
    def to_int(self):
        value = 0
        for byte in self.data:
            # Make sure the byte is a digit
            if byte < 0x31 or byte > 0x39:
                raise Exception("String has non-digit chars")
            digit_value = byte - 0x30
            value = (value * 10) + digit_value
        return value


    def add(self, rhs):
        result = ""
        for i in range(self.data.len()):
            digit1 = self.data[i] - 0x30
        for j in range(rhs):
            digit2 = rhs.data[j] - 0x30

            sum = digit1 + digit2
            if sum > 9:
                #first_digit  =
                second_digit = sum - digit1
                result += str(sum)

def add(str1, str2):
    result = ""
    max = max(len(str1), len(str2))
    complement = 0
    for i in range(max)[::-1]:
        if i >= str1.len():
            digit1 = 0
        else:
            digit1 = str1[i] - 0x30
        if i >= str2.len():
            digit2 = 0
        else:
            digit2 = str2[i] - 0x30
        sum = digit1 + digit2 + complement
        complement = 0
        if sum > 9:
            complement = 1
            sum -= 10
        result += str(sum)
    if complement != 0:
        result += str(1)
    return result[::-1]


    def binary_to_int(self):
        value = 0
        for byte in self.data:
            # Make sure the byte is a digit
            if byte < 0x31 or byte > 0x39:
                raise Exception("String has non-digit chars")
            digit_value = byte - 0x30
            value = (value * 2) + digit_value
        return value


def divide_str(str1, str2):
    result = ''
    divider = str1 - 0x30
    accumlator = 0
    for i in str2 - 0x30:
        if accumlator >= divider:
            quotient = accumlator // divider
            accumlator = accumlator % divider
            result += str(quotient)

        digit = str2[i] - 0x30
        accumlator += (accumlator * 10) + digit
    if accumlator != 0:
        result += str(accumlator // 10)
    return result

result = divide_str('5', '345')
print(result)



#TODO- impliment devide with 2 intigers

def devide_int(int1,int2):
    result =''
    devider = int1
    accumlator = 0
    for i in range(int2):
        if accumlator >= devider:
            quotient = accumlator // int1
            accumlator = accumlator % int1
            result += str(quotient)
        digit = int2[i]
        accumlator += (accumlator * 10) + digit
        if accumlator != 0:
            result += accumlator // 10
    return result





















'''
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



























































































