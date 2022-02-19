import argparse


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
                        help="The number of Carriers of your fleet. The size of a Carrier is 5",
                        type=int,
                        default=0)

    parser.add_argument("-s2", "--battleships",
                        help="The number of Battleships of your fleet. The size of a Battleship is 4",
                        type=int,
                        default=0)

    parser.add_argument("-s3", "--submarines",
                        help="The number of Submarines of your fleet. The size of a Submarine is 3",
                        type=int,
                        default=0)

    parser.add_argument("-s4", "--destroyers",
                        help="The number of Destroyers of your fleet. The size of a Destroyer is 2",
                        type=int,
                        default=1)

    parser.add_argument("-o", "--option",
                        help="The variant of the game you want to play: 0 if I have to shoot again after I hit, 1 otherwise",
                        type=int,
                        default=0)

    return parser.parse_args()
