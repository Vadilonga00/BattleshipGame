# This file is for the main execution of the program.

import game_board
import gui
import inputs
import game
import Utils

args = inputs.initialize_parser()

type_list = Utils.create_ship_type_list(args.carriers, args.battleships, args.submarines, args.destroyers)
board_player1, ship_list1 = game_board.create_board(args.rows, args.columns, type_list)
input('\n\nPress enter and pass the computer to the other player:')
print("\n"*30)
board_player2, ship_list2 = game_board.create_board(args.rows, args.columns, type_list)
input('\n\nPress enter and pass the computer to the other player to start playing:')
print("\n"*30)

if args.graphics == 1:
    app = gui.GuiApp(args, ship_list1, ship_list2, board_player1, board_player2)
    app.mainloop()
else:
    play_board1 = [['-'] * args.columns for x in range(args.rows)]
    play_board2 = [['-'] * args.columns for x in range(args.rows)]
    game.start_game(ship_list1, ship_list2, args.rows, args.columns, args.option, play_board1, play_board2)
