import argparse

def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i1", "--rows",
                        help="Number of rows of the board",
                        type=int,
                        default=10)

    parser.add_argument("-i2", "--columns",
                        help="Number of columns of the board",
                        type=int,
                        default=10)

    # TODO: Add an argument for every type of ship (Battleship(size 5), Cruiser(size 4), Submarine(3), Destroyer(2))
    parser.add_argument("-i3", "--ships",
                        help="The number of ships to play with",
                        type=int,
                        default=2)

    parser.add_argument("-i4", "--turns",
                        help="The number of turns a game should last",
                        type=int,
                        default=50)

    return parser.parse_args()

