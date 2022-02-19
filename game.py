import ship_types
import sys
import game_board
import Utils


def player1_shoot(ship_list1, ship_list2, args, play_board1, play_board2):
    """
     a method that asks the player1 for the desired row or column
     then it checks if he's win,has shot or sunk
     :param play_board1: Player1's game board
     :param play_board2: Player2's game board
     :param args: The inputs given by the user
     :param ship_list1: Player1's ship list
     :param ship_list2: Player2's ship list
     :return: A message if player1 wins, hits or sunks a player2's ship or misses the shot
     """
    game_board.print_board(play_board2, args)
    row_guess, col_guess = Utils.choose_and_check_strike_point(args, play_board2)
    player = 1
    for i in ship_list2:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            play_board2[row_guess - 1][col_guess - 1] = 'X'
            if ship_types.Ship.is_sunk(i):
                if is_win(ship_list2):
                    print('\nPlayer1 wins the game')
                    sys.exit()
                else:
                    print('\nHit and sunk a ship!')
                    Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
            else:
                print('\nHit!')
                Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
    print('\nMiss, pass the computer to Player2')
    play_board2[row_guess - 1][col_guess - 1] = 'O'
    player2_shoot(ship_list1, ship_list2, args, play_board1, play_board2)


def player2_shoot(ship_list1, ship_list2, args, play_board1, play_board2):
    """
     A method that asks the player2 for the desired row or column
     then it checks if he's win,has shot or sunk
     :param play_board1: Player1's game board
     :param play_board2: Player2's game board
     :param args: The inputs given by the user
     :param ship_list1: Player1's ship list
     :param ship_list2: Player2's ship list
     :return: A message if player2 wins, hits or sunks a player1's ship or misses the shot
     """
    player = 2
    game_board.print_board(play_board1, args)
    row_guess, col_guess = Utils.choose_and_check_strike_point(args, play_board1)
    for i in ship_list1:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            play_board1[row_guess - 1][col_guess - 1] = 'X'
            if ship_types.Ship.is_sunk(i):
                if is_win(ship_list1):
                    print('\nPlayer2 wins the game')
                    sys.exit()
                else:
                    print('\nHit and sunk a ship!')
                    Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
            else:
                print('\nHit!')
                Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
    print('\nMiss, pass the computer to Player1')
    play_board1[row_guess - 1][col_guess - 1] = 'O'
    player1_shoot(ship_list1, ship_list2, args, play_board1, play_board2)


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

