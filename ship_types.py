from abc import ABC, abstractmethod


class Ship(ABC):
    def __init__(self, size, orientation, start_row, start_col):
        self.size = size
        self.orientation = orientation
        self.start_row = start_row
        self.start_col = start_col

    @abstractmethod
    def create_empty_boat(self):
        pass


class Carrier(Ship):
    def __init__(self, size=5):
        self.size = size
        super().__init__(self)

    @property
    def create_empty_boat(self):
        return 'carrier'


class Battleship(Ship):
    def __init__(self, size=4):
        self.size = size
        super().__init__(self)

    @property
    def create_empty_boat(self):
        return 'battleship'


class Submarine(Ship):
    def __init__(self, size=3):
        self.size = size
        super().__init__(self)

    @property
    def create_empty_boat(self):
        return 'submarine'


class Destroyer(Ship):
    def __init__(self, size=2):
        self.size = size
        super().__init__(self)

    @property
    def create_empty_boat(self):
        return 'destroyer'
