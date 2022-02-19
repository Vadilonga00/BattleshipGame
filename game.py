import ship_types
import sys
import game_board
import Utils


def player_shoot(ship_list, args, play_board, player, game_end):
    hit = False
    game_board.print_board(play_board, args)
    row_guess, col_guess = Utils.choose_and_check_strike_point(args, play_board)
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            hit = True
            play_board[row_guess - 1][col_guess - 1] = 'X'
            if ship_types.Ship.is_sunk(i):
                if is_win(ship_list):
                    print(f'\nPlayer {player} wins the game')
                    game_end = True
                else:
                    print('\nHit and sunk a ship!')
            else:
                print('\nHit!')
    if not hit:
        print('\nMiss!')
        play_board[row_guess - 1][col_guess - 1] = 'O'
    return hit, game_end, player


def start_game(ship_list1, ship_list2, args, play_board1, play_board2):
    print("\n\n\nPlayer 1 will start the game!")
    hit, game_end, player = player_shoot(ship_list2, args, play_board2, 1, game_end=False)
    while not game_end:
        hit, game_end, player = switch_player(hit, player, ship_list1, ship_list2, args, play_board1, play_board2, game_end)
    sys.exit()


def switch_player(hit, player, ship_list1, ship_list2, args, play_board1, play_board2, game_end):
    if player == 1:
        if hit and args.option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list2, args, play_board2, player, game_end)
        else:
            player = 2
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list1, args, play_board1, player, game_end)
    else:
        if hit and args.option == 0:
            print('\nYou can shoot again!')
            hit, game_end, player = player_shoot(ship_list1, args, play_board1, player, game_end)
        else:
            player = 1
            print(f'\nPass the computer to Player {player}')
            hit, game_end, player = player_shoot(ship_list2, args, play_board2, player, game_end)
    return hit, game_end, player

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
