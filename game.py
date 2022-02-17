import ship_types
import sys
import game_board

def player1_shoot(ship_list,args,play_board1,play_board2):
        game_board.print_board(play_board2,args)
        row_guess = int(input("guess_row:\n"))
        col_guess = int(input("guess_column:\n"))
        for i in ship_list:
            if [row_guess, col_guess] in i.coordinates:
                play_board2[row_guess-1][col_guess-1] = 'X'
                i.coordinates.remove([row_guess, col_guess])
                i.hits = i.hits + 1
                if ship_types.Ship.is_sunk(i):
                    if is_win(ship_list):
                        print('Player1 wins the game')
                        sys.exit()
                    else:
                        print('Colpito e affondato, spara di nuovo!')
                        if args.option == 0:
                            player1_shoot(ship_list,args,play_board1,play_board2)
                        else:
                            player2_shoot(ship_list,args,play_board1,play_board2)
                else:
                    print('Colpito, spara di nuovo!')
                    if args.option == 0:
                        player1_shoot(ship_list,args, play_board1,play_board2)
                    else:
                        player2_shoot(ship_list, args, play_board1,play_board2)
            print('Mancato,passa il computer al Player2')
            play_board2[row_guess - 1][col_guess - 1] = 'O'
            player2_shoot(ship_list, args, play_board1,play_board2)





def player2_shoot(ship_list,args,play_board1,play_board2):
        game_board.print_board(play_board1, args)
        row_guess = int(input("guess_row:\n"))
        col_guess = int(input("guess_column:\n"))
        for i in ship_list:
            if [row_guess, col_guess] in i.coordinates:
                play_board1[row_guess - 1][col_guess - 1] = 'X'
                i.coordinates.remove([row_guess, col_guess])
                i.hits = i.hits + 1
                if ship_types.Ship.is_sunk(i):
                    if is_win(ship_list):
                        print('Player2 wins the game')
                        sys.exit()
                    else:
                        print('Colpito e affondato, spara di nuovo!')
                        if args.option == 0:
                            player2_shoot(ship_list,args,play_board1,play_board2)
                        else:
                            player1_shoot(ship_list, args, play_board1,play_board2)
                else:
                    print('Colpito, spara di nuovo!')
                    if args.option == 0:
                        player2_shoot(ship_list,args ,play_board1,play_board2)
                    else:
                        player1_shoot(ship_list, args, play_board1,play_board2)
        print('Mancato,passa il computer al Player1')
        play_board1[row_guess-1][col_guess-1]='O'
        player1_shoot(ship_list, args, play_board1,play_board2)


def is_win(ship_list):
    """
    :param ship_list:the list of ships of the enemy player
    :return: a logical value that returns true if the player won the game
    """
    j = 0
    is_alive = False
    while j < len(ship_list) and not is_alive:
        if not (ship_types.Ship.is_sunk(ship_list[j])):
            is_alive = True
        j = j + 1
    return not is_alive


