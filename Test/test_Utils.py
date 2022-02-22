import unittest

from BattleshipGame.Utils import check_orientation, check_start_point, create_ship_type_list


class TestUtils(unittest.TestCase):
    # Test of Utils.check_orientation

    def test_if_check_orientation_return_true_if_input_given_is_horizontal(self):
        actual = check_orientation(orientation='horizontal')
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_true_if_input_given_is_vertical(self):
        actual = check_orientation(orientation='vertical')
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_false_if_input_given_has_an_integer(self):
        actual = check_orientation(orientation='1234567890')
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_false_if_input_given_has_a_special_character(self):
        actual = check_orientation(orientation='!"£$%&/()=')
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_if_check_start_point_return_true_if_start_col_and_start_row_is_in_range(self):
        self.assertEqual(True, check_start_point(9, 9, 1, 1))
        self.assertEqual(True, check_start_point(9, 9, 2, 3))
        self.assertEqual(True, check_start_point(9, 9, 8, 9))
        self.assertEqual(True, check_start_point(9, 9, 2, 7))
        self.assertEqual(True, check_start_point(9, 9, 3, 3))

    def test_if_check_start_point_return_false_if_start_col_and_start_row_is_not_in_range(self):
        self.assertEqual(False, check_start_point(9, 9, 12, 13))
        self.assertEqual(False, check_start_point(9, 9, 20, 20))
        self.assertEqual(False, check_start_point(9, 9, 17, 30))
        self.assertEqual(False, check_start_point(9, 9, 10, 13))
        self.assertEqual(False, check_start_point(9, 9, 12, 13))

    def test_if_check_start_point_return_false_if_start_col_or_start_row_is_not_in_range(self):
        self.assertEqual(False, check_start_point(9, 9, 1, 13))
        self.assertEqual(False, check_start_point(9, 9, 18, 5))

    def setUp(self):
        self.carriers = 2
        self.battleships = 1
        self.submarines = 1
        self.destroyers = 2

    def test_if_create_ship_type_list_increment_type_list(self):
        self.assertEqual(6,
                         len(create_ship_type_list(self.carriers, self.battleships, self.submarines, self.destroyers)))


if __name__ == '__main__':
    unittest.main()
