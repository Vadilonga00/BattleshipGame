# This file contains the definition and methods of all the ships that a user can create in the game.


# Base Ship class from which every other sub-Ship-class will inherit
class Ship:
    """The constructor which receives:
         :param size: The length of the ship
         :param orientation: The direction of the ship (horizontal or vertical)
         :param start-row/start-col: The starting point of the ship for the positioning
         :param coordinates: A list of the occupied coordinates by the ship
         """

    def __init__(self, size, orientation, start_row, start_col, coordinates=None):
        self.size = size
        self.orientation = orientation
        self.start_row = start_row
        self.start_col = start_col
        self.hits = 0

        if coordinates is None:
            self.coordinates = []
        else:
            self.coordinates = coordinates

    # This method checks if a ship is sunk
    def is_sunk(self):
        if self.hits == self.size:
            return True
        else:
            return False


# All the subclasses need only a default size and the coordinates occupied
class Carrier(Ship):
    def __init__(self, size, orientation, start_row, start_col, coordinates):
        self.size = 5
        super().__init__(size, orientation, start_row, start_col, coordinates)


class Battleship(Ship):
    def __init__(self, size, orientation, start_row, start_col, coordinates):
        self.size = 4
        super().__init__(size, orientation, start_row, start_col, coordinates)


class Submarine(Ship):
    def __init__(self, size, orientation, start_row, start_col, coordinates):
        self.size = 3
        super().__init__(size, orientation, start_row, start_col, coordinates)


class Destroyer(Ship):
    def __init__(self, size, orientation, start_row, start_col, coordinates):
        self.size = size
        super().__init__(size, orientation, start_row, start_col, coordinates)
