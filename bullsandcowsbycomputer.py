import random

class Bulls_and_cows:
    def __init__(self):
        self.count = 22
        self.result = ''
        self.numbers_on_answer = []
        self.not_on_list = []

    def start(self):
        print("Welcome to the game!!\n")
        print(f'The computer guess is {self.computer_guess()}')
        for i in range(self.count):
            self.users_input()
            print(self.guess)
            if self.end_of_game():
                return
        print("Well done! You won")

    def computer_guess(self):
        self.guess = random.sample(range(1, 10), 4)
        return self.guess

    def move_guess_forward(self):
        self.guess = self.guess[1:] + [self.guess[0]]

    def adjust_guess(self):
        self.guess = self.not_on_list[:2] + self.guess[2:]

    def generate_guess_from_answers(self):
        self.guess = ''.join(map(str, self.numbers_on_answer))



    def users_input(self):
        self.bulls = int(input('Enter how many bulls: '))
        self.cows = int(input('Enter how many cows: '))
        if self.bulls == 1:
            self.move_guess_forward()
            self.adjust_guess()
            if self.cows == 0:
                self.guess[3].append(self.numbers_on_answer)
            elif self.move_guess_forward():
                self.adjust_guess()
                if self.cows == 0:
                    self.guess[2].append(self.numbers_on_answer)
                elif self.move_guess_forward():
                    self.adjust_guess()
                    if self.cows == 0:
                        self.guess[1].append(self.numbers_on_answer)
                    else: self.guess[0].append(self.numbers_on_answer)

        elif self.bulls == 2:
            self.move_guess_forward()
            self.adjust_guess()
            if self.cows == 2:
                self.not_on_list.append(self.guess[3])
                self.move_guess_forward()
                self.adjust_guess()
                if self.cows == 2:
                    self.not_on_list.append(self.guess[2])
                    #here we know that only two digits are left therfore they're the two cows
                    self.not_on_list.append(self.guess[0])
                    self.not_on_list.append(self.guess[1])
                if self.cows == 1:
                    self.not_on_list.append(self.guess[2])
                    self.move_guess_forward()
                    self.adjust_guess()
                    if self.cows == 1:
                        self.not_on_list.append(self.guess[1])
                        self.not_on_list.append(self.guess[0])



        elif self.bulls == 3:
            self.move_guess_forward()
            self.adjust_guess()
            if self.cows == 3:
                self.not_on_list.append(self.guess[3])
            if self.cows == 2:
                self.not_on_list.append(self.guess[2])
                # here we know that only two digits are left therfore they're the two cows
                self.not_on_list.append(self.guess[0])
                self.not_on_list.append(self.guess[1])
            if self.cows == 1:
                self.not_on_list.append(self.guess[2])
                self.move_guess_forward()
                self.adjust_guess()
                if self.cows == 1:
                    self.not_on_list.append(self.guess[1])
                    self.not_on_list.append(self.guess[0])

        else:
            self.end_of_game()

    def end_of_game(self):
        if self.bulls == 4:
            print("The computer beat you")
            return True
        if self.count <= 0:
            print('the computer lost')
        return False

game = Bulls_and_cows()
game.start()

'''                if self.cows == 0:
                    self.guess.append(self.not_on_list)
                    self.computer_guess() '''