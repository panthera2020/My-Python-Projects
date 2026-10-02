import unittest

import sneaky_seven
from sneaky_seven import SneakySeven


class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.sneaky_seven = SneakySeven()
        self.number = 20

    def test_that_when_i_get_a_number_returns_list_of_numbers_divisible_by_seven_from_one_to_number(self):
        self.assertEqual([7,14], self.sneaky_seven.get_numbers_divisible_by_seven_in(self.number))

    def test_that_when_i_get_a_number_returns_true_if_it_contains_seven(self):
        number = 171
        self.assertTrue(self.sneaky_seven.contains_seven(number))

    def test_that_when_i_get_a_number_returns_false_if_it_contains_seven(self):
        number = 100
        self.assertFalse(self.sneaky_seven.contains_seven(number))

    def test_that_when_i_get_a_number_returns_list_of_numbers_that_contain_seven_from_one_to_number(self):
        self.assertEqual([7,17], self.sneaky_seven.get_numbers_that_contains_seven_in(self.number))

    def test_that_when_i_get_a_number_returns_list_of_numbers_that_contain_seven_and_divisible_by_seven(self):
        self.assertEqual([7,14,17], self.sneaky_seven.get_numbers_that_contains_seven_and_divisible_by_seven_in(self.number) )

    def test_that_when_i_get_a_number_returns_list_of_numbers_that_contain_seven_and_divisible_by_seven_but_not_both(self):
        self.assertEqual([14,17], self.sneaky_seven.get_numbers_that_contains_seven_and_divisible_by_seven_not_both_in(self.number))

    def test_that_a_number_return_count_of_numbers_that_contain_seven_and_divisible_by_seven_but_not_both_from_one_to_number(self):
        self.assertEqual(2,self.sneaky_seven.count_sneaky_seven(self.number))
        self.assertEqual(10,self.sneaky_seven.count_sneaky_seven(50))

if __name__ == '__main__':
    unittest.main()
