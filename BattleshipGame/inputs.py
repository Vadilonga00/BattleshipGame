import argparse
import sys


def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--rows",
                        help="Number of rows of the board",
                        type=int,
                        default=9)

    parser.add_argument("-c", "--columns",
                        help="Number of columns of the board",
                        type=int,
                        default=9)

    parser.add_argument("-s1", "--carriers",
                        help="The number of Carriers of your fleet, if not specified, equal to 1. The size of a "
                             "Carrier is 5.",
                        type=int,
                        default=2)

    parser.add_argument("-s2", "--battleships",
                        help="The number of Battleships of your fleet, if not specified, equal to 1. The size of a "
                             "Battleship is 4",
                        type=int,
                        default=0)

    parser.add_argument("-s3", "--submarines",
                        help="The number of Submarines of your fleet, if not specified, equal to 1. The size of a "
                             "Submarine is 3",
                        type=int,
                        default=0)

    parser.add_argument("-s4", "--destroyers",
                        help="The number of Destroyers of your fleet, if not specified, equal to 1. The size of a "
                             "Destroyer is 2",
                        type=int,
                        default=1)

    parser.add_argument("-o", "--option",
                        help="The variant of the game you want to play: 0 if after a Hit you can shoot again, "
                             "1 otherwise",
                        type=int,
                        default=0)

    parser.add_argument("-g", "--graphics",
                        help="If you want to play with graphical interface use 1. If not use 0 or don't call this "
                             "parameter",
                        type=int,
                        default=1)

    return parser.parse_args()


def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    if not 0 < args.rows < 100:
        print('\u001b[31mInvalid number of rows\033[0m')
        raise ValueError
    if not 0 < args.columns < 100:
        print('\u001b[31mInvalid number of columns\033[0m')
        raise ValueError
    if not 0 <= args.carriers < 2:
        print('\u001b[31mInvalid number of carriers\033[0m')
        raise ValueError
    if not 0 <= args.battleships < 3:
        print('\u001b[31mInvalid number of battleships\033[0m')
        raise ValueError
    if not 0 <= args.submarines < 4:
        print('\u001b[31mInvalid number of submarines\033[0m')
        raise ValueError
    if not 0 <= args.destroyers < 5:
        print('\u001b[31mInvalid number of destroyers\033[0m')
        raise ValueError
    if not (args.option == 0 or args.option == 1):
        print('\u001b[31mInvalid input "option". It must be 0 or 1\033[0m')
        raise ValueError
    if not (args.graphics == 0 or args.graphics == 1):
        print('\u001b[31mInvalid input "graphics". It must be 0 or 1\033[0m')
        raise ValueError
