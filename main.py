import Utils
import inputs
args = inputs.initialize_parser()

ship_list = []
type_list = Utils.create_ship_type_list(args)
board_player1 = Utils.create_board(args, type_list)
print('Pass now the computer to the other player!')
board_player2 = Utils.create_board(args, type_list)
Utils.gameplay(args, ship_list)




