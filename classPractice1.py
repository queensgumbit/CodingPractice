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
