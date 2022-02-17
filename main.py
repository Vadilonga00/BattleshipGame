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
play_board1 = board = [['-'] * args.columns for x in range(args.rows)]
play_board2 = board = [['-'] * args.columns for x in range(args.rows)]
#Start the game, player_1 starts
game.player1_shoot(ship_list2, args, play_board1, play_board2)




