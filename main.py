# This file is for the main execution of the program.

import game_board
import inputs
import game
import Utils


args = inputs.initialize_parser()

type_list = Utils.create_ship_type_list(args)
board_player1, ship_list1 = game_board.create_board(args, type_list)
print('\n\n\n\nPass now the computer to the other player!')
board_player2, ship_list2 = game_board.create_board(args, type_list)
#Start the game, player_1 starts
for i in range(args.turns):
    game.player1_shoot(ship_list2)
    game.player2_shoot(ship_list1)





