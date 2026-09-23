import unittest

from filter import *

class MyTestCase(unittest.TestCase):
    def test_thatWhenInputANumberItReturnsTrue(self):
        self.filter = filter_one()
        self.assertTrue(self.filter.is_digit(1))

    def test_thatWhenInuptIsNotADigitReturnsFalse(self):
        self.filter = filter_one()
        self.assertFalse(self.filter.is_digit(None))

    def test_thatWhenIGetAListOfInput_returnsListOfDigits(self):
        self.filter = filter_one()
        self.assertEqual([1,3,5],self.filter.get_digits([1,None,3,None,5]))

    def test_thatWhenNumberIsDivisibleByThree_returnsTrue(self):
        self.filter = filter_two()
        self.assertTrue(self.filter.is_divisible_by_three(9))

    def test_thatWhenIGetListOfNumber_returnsNumbersDivisibleByThree(self):
        self.filter = filter_two()
        self.assertEqual([3,6,9,12],self.filter.get_numbers_divisible_by_three([1,3,4,6,9,12]))

    def test_thatWhenNumberIsPositive_returnsTrue(self):
        self.filter = filter_three()
        self.assertTrue(self.filter.is_positive(6))

    def test_thatWhenNumberIsNegative_returnsFalse(self):
        self.filter = filter_three()
        self.assertFalse(self.filter.is_positive(-1))

    def test_thatWhenIGetAListOfNumber_returnsNumbersPositive(self):
        self.filter = filter_three()
        self.assertEqual([0,1,2], self.filter.get_positive_numbers([-2,-1,0,1,2]))

    def test_thatWhenIGetADictionary_returnsTrueIfValueIsGreaterThan25(self):
        self.filter = filter_four()
        self.assertTrue(self.filter.is_value_greater_than_25({'name':"Alice",'age':30}))

    def test_thatWhenIGetAListOfDictionary_returnsListWithValuesGreaterThan25(self):
        self.filter = filter_four()
        self.assertEqual([{'name':"Alice",'age':30}],self.filter.get_element_greater_than_25([{'name':"Alice",'age':30},{'name':"Bob",'age':20}]))


