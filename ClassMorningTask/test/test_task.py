import unittest

from task import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(9, digit_sum_number_until_single_digit(999))
        self.assertEqual(7, digit_sum_number_until_single_digit(7))


if __name__ == '__main__':
    unittest.main()
