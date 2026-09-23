import unittest

from reduce import *

class MyTestCase(unittest.TestCase):
    def test_thatWhenIGetAListOfNumber_returnsAProductOfAllNumbers(self):
        self.reduce = reduce_one()
        self.assertEqual(24,self.reduce.get_product([2,3,4]))

    def test_thatWhenIGetAListOfNumber_returnsMaximumNumber(self):
        self.reduce = reduce_two()
        self.assertEqual(9,self.reduce.get_maximum_value([3,7,2,9,1]))

    def test_thatWhenIGetAListOfString_returnsStringsConcatenated(self):
        self.reduce = reduce_three()
        self.assertEqual("Hello World", self.reduce.concatenate(["Hello"," ", "World"]))

    def test_thatWhenIGetAListOfNumbers_returnsSumOfSquares(self):
        self.reduce = reduce_four()
        self.assertEqual(14,self.reduce.sum_of_squares([1,2,3]))

    def test_thatWhenIGetAListOfDictionaries_returnsDictionariesConcatenated(self):
        self.reduce = reduce_five()
        self.assertEqual({"abc": 6 }, self.reduce.compress([{"a": 1},{"b": 2},{"c": 3}]))