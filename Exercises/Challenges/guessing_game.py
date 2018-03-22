import random


class Game:

    RULES = """
            <--------------------------------GUESS THE NUMBER-------------------------------->
            Welcome to Guess the Number!                                       
            I'm going to think of a number between 1 and 100                    
            while you try and guess what it is! Remember,                       /\-/\ 
            you cannot guess a number less than 1 or greater than 100!         (=^Y^=)
            I'll give you hints with each guess on how close you are to         (>o<)
            guessing my number. When you finally guess it, i'll tell
            you how many guesses it took! Good luck!
            <--------------------------------+++++++++++++++-------------------------------->
            
            """

    def __init__(self, player):
        self.player = player
        self.mystery_number = random.randint(1, 100)

    def start_game(self):
        print(Game.RULES)

    def is_in_range(self, player_number, mystery_number):
        return abs(mystery_number - player_number) in range(1, 11)

    def play_round(self):
        pass

    def get_previous_guess(self, guess_list):
        return guess_list[-1]

    def game_stats(self, guess_list):
        for index, value in enumerate(guess_list, start=1):
            print('On turn {} you guessed {}'.format(index, value))

    def next_round(self, guess_list):
        pass






class Player:

    def __init__(self):
        self.guesses = []

    def is_first_round(self):
        return len(self.guesses) == 0

    def add_to_guess_list(self, number):
        return self.guesses.append(number)

    def get_total_guess_count(self):
        return len(self.guesses)












