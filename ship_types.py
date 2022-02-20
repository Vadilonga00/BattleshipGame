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
        """
        This method checks if the ship is sunk
        :return: A Boolean value: True if the ship is sunk, False otherwise
        """
        if self.hits == self.size:
            return True
        else:
            return False

    def is_hit(self, row_guess, col_guess):
        """
        This method verifies if the shot given is a hit. If it is, removes from the ship the coordinates of the hit and
        increments the number of hits taken
        :param row_guess: The row coordinate of the shot
        :param col_guess: The column coordinate of the shot
        :return: A Boolean value: True if the ship is hit, False otherwise
        """
        if self.check_hit(row_guess, col_guess):
            self.coordinates.remove([row_guess, col_guess])
            self.hits += 1
            return True
        return False

    def check_hit(self, row_guess, col_guess):
        """
        This method checks if the shot given is a hit
        :param row_guess: The row coordinate of the shot
        :param col_guess: The column coordinate of the shot
        :return: A Boolean value: True if the ship is hit, False otherwise
        """
        if [row_guess, col_guess] in self.coordinates:
            return True
        return False


# All the subclasses need only a default size
class Carrier(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(5, orientation, start_row, start_col, coordinates)


class Battleship(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(4, orientation, start_row, start_col, coordinates)


class Submarine(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(3, orientation, start_row, start_col, coordinates)


class Destroyer(Ship):
    def __init__(self, orientation, start_row, start_col, coordinates):
        super().__init__(2, orientation, start_row, start_col, coordinates)
