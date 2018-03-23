import random


class Game:

    RULES = """
    
            I'm going to think of a number between 1 and 100                    
            while you try and guess what it is! Remember,                       
            you cannot guess a number less than 1 or greater than 100!         
            I'll give you hints with each guess on how close you are to         
            guessing my number. When you finally guess it, i'll tell
            you how many guesses it took! Good luck!
            
            """

    def __init__(self, player):
        self.player = player
        self.current_guess = None
        self.mystery_number = random.randint(1, 100)

    def start_game(self):
        print(Game.RULES)

    def get_valid_player_guess(self):
        while True:
            try:
                player_input = int(input("What is my number? "))

            except ValueError:
                print("Oops! That was not a valid number, try again...")
                continue

            if self.valid_guess(player_input):
                self.current_guess = player_input
                return self.current_guess

            else:
                print("OUT OF BOUNDS!")

    def valid_guess(self, number):
        if 1 <= number <= 100:
            return True
        return False

    def add_to_guess_list(self, guess_list):
        return guess_list.append(self.current_guess)

    def correct_number(self):
        return self.current_guess == self.mystery_number

    def is_in_range(self, player_number):
        return abs(self.mystery_number - player_number) in range(1, 11)

    def play_round(self):
        pass

    def previous_guess(self, guess_list):
        return guess_list[-1]

    def game_stats(self, guess_list):
        for index, value in enumerate(guess_list, start=1):
            print('On turn {} you guessed {}'.format(index, value))

    def current_status(self, guess_list):
        if abs(self.mystery_number - self.current_guess) < abs(self.mystery_number - self.previous_guess(guess_list)):
            return True
        return False


class Player:

    def __init__(self):
        self.guesses = [0]

    def first_round(self):
        return len(self.guesses) == 1

    def total_guess_count(self):
        return len(self.guesses)












