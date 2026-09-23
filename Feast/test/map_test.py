import unittest

from map import *

class map_test(unittest.TestCase):
    def test_thatWhenIGetAStringAsInteger_returnsInteger(self):
        self.map = map_one()
        self.assertEqual(1,self.map.to_integer("1"))

    def test_thatWhenIGetAListOfStringsAsIntegers_returnsListOfIntegers(self):
        self.map = map_one()
        self.assertEqual([1,2,3],self.map.list_to_integer(["1","2","3"]))

    def test_thatWhenIGetANumber_tenIsAdded(self):
        self.map = map_two()
        self.assertEqual(10,self.map.add_ten(0))

    def test_thatWhenIGetAListOfNumber_tenIsAddedToEachElement(self):
        self.map = map_two()
        self.assertEqual([10,15,20],self.map.add_ten_to([0,5,10]))

    def test_thatWhenIGetANumberInCelcius_returnInFarenheit(self):
        self.map = map_three()
        self.assertEqual(68,self.map.to_farenheit(20))

    def test_thatWhenIGetAListOfNumberInCelcius_returnsListInFarenheit(self):
        self.map = map_three()
        self.assertEqual([68,86],self.map.to_farenheits([20,30]))