from guessing_game import Game
from guessing_game import Player

# STEPS
# Show rules
# Get valid player guess
# Add valid guess to guess list
# Determine if this is the player's first round
    # IF first round
        # IF in range
            # WARM!
        # ELSE
            # COLD!
    # Add guess to guess list

    # IF not first round
        # IF guess is closer to the number than previous guess



player = Player()
game = Game(player)


game.start_game()
print(game.mystery_number)
game.get_valid_player_guess()

while not game.correct_number():

    if player.first_round():
        if game.is_in_range(game.current_guess):
            print("WARM!")
        else:
            print("COLD!")

    if not player.first_round():
        game.get_valid_player_guess()

        if game.current_status(player.guesses):
            print("WARMER!")
        else:
            print("COLDER!")

    game.add_to_guess_list(player.guesses)

print("You got it! It took you {} try(s)".format(player.total_guess_count()))











