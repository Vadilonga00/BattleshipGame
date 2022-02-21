import ship_types
import sys
import game_board
import Utils


def player_shoot(ship_list, args, play_board, player, game_end):
    """
         This method asks the player for the desired row or column for his shot
         then it checks if the shot is a hit, miss, sunks a ship or wins him the game
         :param ship_list: The player's ship list
         :param args: The inputs given by the user
         :param play_board: The player's game board
         :param player: The player shooting
         :param game_end: True if the game is finished, False otherwise
         :return: A console message to describe what the shot did
         :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
         :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
         :return: player: Integer value that represents the player who has just shot. As only to players can play
            this game it can be either 1 or 2
         """
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
    """
    This function starts the game in a Console mode and terminates the program as soon as the game ends
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param args: The inputs given to the program by the user
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :return: None
    """
    print("\n\n\n\n\n\nPlayer 1 will start the game!")
    hit, game_end, player = player_shoot(ship_list2, args, play_board2, 1, game_end=False)
    while not game_end:
        hit, game_end, player = switch_player(hit, player, ship_list1, ship_list2, args, play_board1, play_board2, game_end)
    sys.exit()


def switch_player(hit, player, ship_list1, ship_list2, args, play_board1, play_board2, game_end):
    """
    This function decides when to switch player turn depending on:
        1) If it's a hit or a miss
        2) The option parameter given to the program
    :param hit: True if the last shot was a hit, False otherwise
    :param player: The player who shot last turn
    :param ship_list1: Player 1's Ship list
    :param ship_list2: Player 2's Ship list
    :param args: The inputs given to the program by the user
    :param play_board1: Player 1's game board
    :param play_board2: Player 2's game board
    :param game_end: True if the game is finished, False otherwise
    :return: hit: Boolean value for the hit. True if the shot hits a ship, False otherwise
    :return: game_end: Boolean value for that describes if a game finished (True) or not (False)
    :return: player: The same or the other player depending on the result of the function
    """
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
