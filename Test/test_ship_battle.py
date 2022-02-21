import unittest
import Utils


class TestBattleShip(unittest.TestCase):
    # Test of Utils.check_orientation

    def test_if_check_orientation_return_true_if_input_given_is_horizontal(self):
        actual = Utils.check_orientation(orientation='horizontal')
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_true_if_input_given_is_vertical(self):
        actual = Utils.check_orientation(orientation='vertical')
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_false_if_input_given_has_an_integer(self):
        actual = Utils.check_orientation(orientation='1234567890')
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_if_check_orientation_return_false_if_input_given_has_a_special_character(self):
        actual = Utils.check_orientation(orientation='!"£$%&/()=')
        expected: bool = False
        self.assertEqual(actual, expected)

