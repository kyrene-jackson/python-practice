# The Challenge:
#
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#    within 10 of the number, return "WARM!"
# 3. further than 10 away from the number, return "COLD!"
# 4. On all subsequent turns, if a guess is
#    closer to the number than the previous guess return "WARMER!"
# 5. farther from the number than the previous guess, return "COLDER!"
# 6. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# ----------------------------------------------------------------------------------------------------------------------

import random

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable

# mystery_num = random.randint(1, 100)

# Next, print an introduction to the game and explain the rules

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

# Create a list to store guesses

# guesses = [0]

# Write a while loop that asks for a valid guess. Test it a few times to make sure it works.

# while len(guesses):
#     input("Enter your guess! ")

# Write a while loop that compares the player's guess to our number.




# If the player guesses correctly, break from the
# loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
# -----------

# METHODS


def random_number():
    return random.randint(1, 100)


def show_rules():
    print(RULES)


# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
def guess_in_range(number):
    return number in range(1, 101)

# 2. On a player's first turn, if their guess is
#    within 10 of the number, return "WARM!"


def play_first_turn(player_number, mystery_number):
    if abs(mystery_number - player_number) not in range(1, 11):
        print("COLD!")
    else:
        print("WARM!")


# compare guessed number to previous guess

def play_turn(guess_list, player_number):
    print('Your last guess was {}'.format(guess_list[-1]))
    print('Your current guess is {}'.format(player_number))





def show_guess_list(guess_list):
    for index, value in enumerate(guess_list):
        print('On turn {} you guessed {}'.format(index, value))



def add_to_guess_list(guess_list, number):
    return guess_list.append(number)






def play_game():

    guesses = []
    mystery_number = random_number()

    show_rules()

    while True:
        if len(guesses) == 0:
            try:
                print('DEBUG: mystery number is {}'.format(mystery_number)) # 56
                player_guess = int(input("Enter your guess: ")) # 54
                if player_guess == mystery_number:
                    print('Hey you guessed it! It took you {} try(s)'.format(len(guesses)))
                    break
                elif guess_in_range(player_guess): # True
                    play_first_turn(player_guess, mystery_number)  # WARM!
                    add_to_guess_list(guesses, player_guess)
                else:
                    print("OUT OF BOUNDS")
                    add_to_guess_list(guesses, player_guess)

            except ValueError:
                print("Oops! That was not a valid number, try again...")

        else:
            print('Next Round....')
            print('DEBUG: guess list length is {}'.format(len(guesses)))
            player_guess = int(input("Enter your next guess: "))
            if player_guess == mystery_number:
                print('Hey you guessed it! It took you {} try(s)'.format(len(guesses)))
                break
            elif guess_in_range(player_guess):
                play_turn(guesses, player_guess)
                add_to_guess_list(guesses, player_guess)
                show_guess_list(guesses)




# RUNNER
play_game()






