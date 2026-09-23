import unittest

from split_word import split_word

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.split_word = split_word()

    def test_thatWhenIGetAWordAndACharcterInWord_returnTheWordSplitFromRightToLeft(self):
        self.assertEqual("dcba", self.split_word.split_word_left("abcdefgh", "d"))

    def test_thatWhenIGetAWordAndCharcterInWord_returnTheWordSplitFromLeftToRight(self):
        self.assertEqual("hgfed",self.split_word.splt_word_right("abcdefgh",'d'))

    def test_thatWhenIGetAWordAndCharcterInWord_returnTheWordSplitFromCharacterToLeftAndBackToCharacter(self):
        self.assertEqual("dcbahgfed",self.split_word.splt_word_round("abcdefgh",'d'))

    def test_thatWhenIGetAWordAndIGetCharacterNotInWord_returnWord(self):
        self.assertEqual("abcdefgh", self.split_word.splt_word_round("abcdefgh", 'i'))

