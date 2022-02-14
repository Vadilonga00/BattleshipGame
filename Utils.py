# This file contains a collection of utilities methods for the other files and classes
import ship_types


def check_orientation(orientation):
    if orientation == 'horizontal' or orientation == 'vertical':
        return True
    else:
        return False


def check_start_point(args, start_row, start_col):
    if start_row <= args.rows and start_col <= args.columns:
        return True
    else:
        return False


def create_ship_type_list(args):
    type_list = []
    counter = 0
    while counter < args.carriers:
        new = 5
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships:
        new = 4
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships + args.submarines:
        new = 3
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships + args.submarines + args.destroyers:
        new = 2
        type_list.append(new)
        counter += 1
    return type_list


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
