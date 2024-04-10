import random


class Bulls_and_Cows:
    def __init__(self):
        self.unique_digits = random.sample(range(10), 4)
        self.four_digit_number_unique = ''.join(map(str, self.unique_digits))
        self.result = ''
        self.count = 15 #15 chances to guess

    def start(self):
        print("Welcome to the game!!\n")
        print(f'the number : {self.four_digit_number_unique}')
        for i in range(self.count):
            self.get_user_input()
            print("LALA", self.guess_of_numbers)
            self.check_guess()
            if self.end_of_game():
                return
            print(f'you have {self.bulls} digit/s in the right place, and {self.cows} right digit/s in the wrong place')
        print(f"You've used up all your guesses. Game over.\nthe number was {self.four_digit_number_unique}")

    def get_user_input(self):
        guess_of_numbers = ""
        invalid_guess = False
        while len(guess_of_numbers) != 4 or not guess_of_numbers.isdigit():
            if invalid_guess:
                print("Incorrect input try again\n")
            guess_of_numbers = input('whats your guess?')
            invalid_guess = True
        self.guess_of_numbers = guess_of_numbers
        return

    def check_guess(self):
        self.bulls = sum([a == b for a, b in zip(self.guess_of_numbers, self.four_digit_number_unique)])
        self.cows = sum([min(self.four_digit_number_unique.count(digit), self.guess_of_numbers.count(digit)) for digit in set(self.guess_of_numbers)]) - self.bulls
        return


    def end_of_game(self):
        if self.bulls == len(self.unique_digits):
            print(f'you have guessed right the number - {self.four_digit_number_unique}\nWell done!')
            return True
        return False

user1 = Bulls_and_Cows()
user1.start()
