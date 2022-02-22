import unittest
from BattleshipGame import ship_types


class TestShipTypes(unittest.TestCase):

    # Create a set of ships that will be reused all over the tests
    def setUp(self):

        self.ship = ship_types.Ship(2, None, 1, 1, [[1, 1], [1, 2]])
        self.carrier = ship_types.Carrier(None, 1, 1, [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])
        self.battleship = ship_types.Battleship(None, 1, 1, [[1, 1], [1, 2], [1, 3], [1, 4]])
        self.submarine = ship_types.Submarine(None, 1, 1, [[1, 1], [1, 2], [1, 3]])
        self.destroyer = ship_types.Destroyer(None, 1, 1, [[1, 1], [1, 2]])

    def tearDown(self):
        pass

    def test_if_check_hit_returns_True_on_hit(self):

        self.assertEqual(True, ship_types.Ship.check_hit(self.ship, 1, 1))
        self.assertEqual(True, ship_types.Carrier.check_hit(self.carrier, 1, 5))
        self.assertEqual(True, ship_types.Battleship.check_hit(self.battleship, 1, 2))
        self.assertEqual(True, ship_types.Submarine.check_hit(self.submarine, 1, 3))
        self.assertEqual(True, ship_types.Destroyer.check_hit(self.destroyer, 1, 2))

    def test_if_check_hit_returns_False_on_miss(self):

        self.assertEqual(False, ship_types.Ship.check_hit(self.ship, 1, 3))
        self.assertEqual(False, ship_types.Carrier.check_hit(self.carrier, 9, 9))
        self.assertEqual(False, ship_types.Battleship.check_hit(self.battleship, 2, 2))
        self.assertEqual(False, ship_types.Submarine.check_hit(self.submarine, 2, 3))
        self.assertEqual(False, ship_types.Destroyer.check_hit(self.destroyer, 5, 5))

    def test_if_is_hit_returns_True_on_hit(self):

        self.assertEqual(True, ship_types.Ship.is_hit(self.ship, 1, 1))
        self.assertEqual(True, ship_types.Carrier.is_hit(self.carrier, 1, 5))
        self.assertEqual(True, ship_types.Battleship.is_hit(self.battleship, 1, 2))
        self.assertEqual(True, ship_types.Submarine.is_hit(self.submarine, 1, 3))
        self.assertEqual(True, ship_types.Destroyer.is_hit(self.destroyer, 1, 2))

    # First hit the ship and then check if the hit number is increased
    def test_if_is_hit_increments_hits_value_of_the_ship_shot(self):

        ship_types.Ship.is_hit(self.ship, 1, 1)
        self.assertEqual(1, self.ship.hits)

        ship_types.Ship.is_hit(self.carrier, 1, 1)
        self.assertEqual(1, self.carrier.hits)

        ship_types.Ship.is_hit(self.battleship, 1, 1)
        self.assertEqual(1, self.battleship.hits)

        ship_types.Ship.is_hit(self.submarine, 1, 1)
        self.assertEqual(1, self.submarine.hits)

        ship_types.Ship.is_hit(self.destroyer, 1, 1)
        ship_types.Ship.is_hit(self.destroyer, 1, 2)
        self.assertEqual(2, self.destroyer.hits)

    # First hit the ship and then check if the hit coordinate has been removed form the ship coordinates list
    def test_if_is_hit_deletes_the_hit_coordinate_of_the_ship(self):

        ship_types.Ship.is_hit(self.ship, 1, 1)
        self.assertEqual(False, [1, 1] in self.ship.coordinates)

        ship_types.Ship.is_hit(self.carrier, 1, 5)
        self.assertEqual(False, [1, 5] in self.carrier.coordinates)

        ship_types.Ship.is_hit(self.battleship, 1, 3)
        self.assertEqual(False, [1, 3] in self.battleship.coordinates)

        ship_types.Ship.is_hit(self.submarine, 1, 2)
        self.assertEqual(False, [1, 2] in self.submarine.coordinates)

        ship_types.Ship.is_hit(self.destroyer, 1, 1)
        self.assertEqual(False, [1, 1] in self.destroyer.coordinates)

    def test_if_is_hit_returns_False_on_miss(self):

        self.assertEqual(False, ship_types.Ship.is_hit(self.ship, 1, 8))
        self.assertEqual(False, ship_types.Carrier.is_hit(self.carrier, 1, 6))
        self.assertEqual(False, ship_types.Battleship.is_hit(self.battleship, 2, 2))
        self.assertEqual(False, ship_types.Submarine.is_hit(self.submarine, 3, 3))
        self.assertEqual(False, ship_types.Destroyer.is_hit(self.destroyer, 4, 2))

    # Miss and then check if hit count is unchanged
    def test_if_is_hit_leaves_hits_value_of_the_ship_unchanged_on_miss(self):

        ship_types.Ship.is_hit(self.ship, 2, 1)
        self.assertEqual(0, self.ship.hits)

        ship_types.Ship.is_hit(self.carrier, 3, 1)
        self.assertEqual(0, self.carrier.hits)

        ship_types.Ship.is_hit(self.battleship, 5, 1)
        self.assertEqual(0, self.battleship.hits)

        ship_types.Ship.is_hit(self.submarine, 1, 7)
        self.assertEqual(0, self.submarine.hits)

        ship_types.Ship.is_hit(self.destroyer, 1, 6)
        ship_types.Ship.is_hit(self.destroyer, 6, 2)
        self.assertEqual(0, self.destroyer.hits)

    def test_if_is_hit_leaves_the_coordinates_of_the_ship_unchanged_on_miss(self):

        ship_types.Ship.is_hit(self.ship, 4, 1)
        self.assertEqual(True, [1, 1] in self.ship.coordinates)
        self.assertEqual(True, [1, 2] in self.ship.coordinates)

        ship_types.Ship.is_hit(self.destroyer, 8, 8)
        self.assertEqual(True, [1, 1] in self.destroyer.coordinates)
        self.assertEqual(True, [1, 2] in self.destroyer.coordinates)

    # Create a list of ships and then hit all of their coordinates. Then check if all are sunk
    def test_if_is_sunk_returns_True_when_the_ship_is_sunk(self):

        ships = [ship_types.Ship(2, None, 1, 1, [[1, 1], [1, 2]]),
                 ship_types.Destroyer(None, 1, 1, [[1, 1], [1, 2]])]
        for ship in ships:
            ship.is_hit(1, 1)
            ship.is_hit(1, 2)

        self.assertEqual(True, ship_types.Ship.is_sunk(ships[0]))
        self.assertEqual(True, ship_types.Destroyer.is_sunk(ships[1]))

    def test_if_is_sunk_returns_False_when_the_ship_is_alive(self):

        self.assertEqual(False, ship_types.Ship.is_sunk(self.ship))
        self.assertEqual(False, ship_types.Carrier.is_sunk(self.carrier))
        self.assertEqual(False, ship_types.Battleship.is_sunk(self.battleship))
        self.assertEqual(False, ship_types.Submarine.is_sunk(self.submarine))
        self.assertEqual(False, ship_types.Destroyer.is_sunk(self.destroyer))


if __name__ == '__main__':
    unittest.main()
