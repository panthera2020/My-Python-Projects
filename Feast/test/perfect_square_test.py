import unittest

from perfect_square import perfect_square


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.perfect_square = perfect_square()

    def test_thatWhenIGetANumber_itReturnsTrueForAPerfectSquare(self):
        self.assertTrue(self.perfect_square.is_perfect_number(49))

    def test_thatWhenIGetANumbers_itReturnsFalseFor_numberThatIsNotAPerfectSquare(self):
        self.assertFalse(self.perfect_square.is_perfect_number(8))

    def test_thatWhenIGetAListOfNumbers_IGetAListOfBooleansIfNumberIsPerfectSquareOrNot(self):
        numbers = [4,9,25,49]
        numbers_two = [0,1,2,3,4,9,10,16,25,26]
        expected = [True, True, False,False,True,True,False,True,True,False]
        self.assertEqual([True,True,True,True],self.perfect_square.check_perfect_squares(numbers))
        self.assertEqual(expected,self.perfect_square.check_perfect_squares(numbers_two))
