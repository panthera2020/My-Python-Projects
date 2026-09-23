import unittest

from palindrome import palindrome

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.palindrome = palindrome()

    def test_thatWhenIHaveAWord_returnsTrueIfWordIsPalindrome(self):
        self.assertTrue(self.palindrome.is_palindrome("Madam"))

    def test_thatWhenIHaveWord_returnsFalseIfWordIsNotPalindrome(self):
        self.assertFalse(self.palindrome.is_palindrome("hello"))

    def test_thatWhenIHaveAListOfWords_returnsListOfBooleanIfPalindromeOrNot(self):
        words = ["Madam", "hello","noon", "racecar"]
        self.assertEqual([True,False,True,True],self.palindrome.is_palindrome_in(words))
