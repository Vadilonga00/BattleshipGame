import Utils
import inputs
args = inputs.initialize_parser()

ship_list = []

board_player1 = Utils.create_board(args)
board_player2 = Utils.create_board(args)
Utils.gameplay(args, ship_list)




