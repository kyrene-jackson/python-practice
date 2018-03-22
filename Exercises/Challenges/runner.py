from guessing_game import Game
from guessing_game import Player

# player = Player()
# game = Game(player)
# my_number = 7
# mystery_number = game.mystery_number
#
# print("This is the first round: {}".format(player.is_first_round()))
# print("Mystery Number: {}".format(game.mystery_number))
# print("My Number: {}".format(my_number))
# print("In range?: {}".format(game.is_in_range(my_number, mystery_number)))
#
# player.add_to_guess_list(12)
# player.add_to_guess_list(20)
# game.next_round(player.guesses)

player = Player()
game = Game(player)


game.start_game()
