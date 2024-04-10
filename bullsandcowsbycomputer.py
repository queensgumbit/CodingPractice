import random
from itertools import combinations

class BullsAndCows:
    def __init__(self):
        self.possible_combinations = self.generate_combinations()

    def game(self):
        print("Welcome to Bulls and Cows game!")
        while True:
            guess = self.random_guess()
            print("Computer's guess:", guess)
            bulls = int(input("Enter the number of bulls: "))
            cows = int(input("Enter the number of cows: "))
            if bulls == 4:
                print("Computer guessed correctly! Game over.")
                break
            else:
                self.remove_combinations(guess, bulls, cows)

    def generate_combinations(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        a = combinations(numbers, 4) #using Itertools('combinations') method
        return [''.join(map(str, i)) for i in a]

    def random_guess(self):
        return random.choice(self.possible_combinations)

    def remove_combinations(self, guess, bulls, cows):
        self.possible_combinations = [i for i in self.possible_combinations if
                                      self.calculate_bulls_cows(guess, i) == (bulls, cows)]
        #checkes every combination with the calculate mtd to determine the num of bulls,cows to the current guess against the combintaion

    def calculate_bulls_cows(self, guess, target):
        bulls = sum(1 for i in range(4) if guess[i] == target[i])  #iterates each index in the guess and checks if guess in this index match the target in this index(a possible combination)
        cows = sum((1 for digit in guess if digit in target)) - bulls #iterates each dgit and checks if the digit exist somewhere in the target(a possible combination)
        return bulls, cows

game = BullsAndCows()
game.game()
