import unittest
from card_validation import CardValidation

class TestCardValidation(unittest.TestCase):

    def setUp(self):
        self.credit_card = CardValidation()

    def test_thatWhenDigitAreInputted_andTheyAreNotUpToRequiredLength_cardLengthIsInvalid(self):
        self.assertFalse(self.credit_card.is_length_valid(5399833))

    def test_thatWhenDigitAreInputted_iGetCardLength(self):
        self.assertEqual(16, self.credit_card.get_length(5399831619690403))

    def test_thatWhenDigitAreInputted_andTheyAreUpToRequiredLength_cardIsValid(self):
        self.assertTrue(self.credit_card.is_length_valid(539987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs4_cardIsValid(self):
        self.assertTrue(self.credit_card.is_length_valid(439987465855678))
        self.assertTrue(self.credit_card.is_first_digit_valid(439987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs5_cardIsValid(self):
        self.assertTrue(self.credit_card.is_length_valid(539987465855678))
        self.assertTrue(self.credit_card.is_first_digit_valid(539987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs6_cardIsValid(self):
        self.assertTrue(self.credit_card.is_length_valid(639987465855678))
        self.assertTrue(self.credit_card.is_first_digit_valid(639987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs3_andSecondDigitIs7_cardIsValid(self):
        self.assertTrue(self.credit_card.is_length_valid(379987465855678))
        self.assertTrue(self.credit_card.is_first_digit_valid(379987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs4_cardTypeIsVisa(self):
        self.assertEqual("Visa", self.credit_card.card_type(439987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs5_cardTypeIsMasterCard(self):
        self.assertEqual("MasterCard", self.credit_card.card_type(539987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs6_cardTypeIsDiscoverCard(self):
        self.assertEqual("Discover Card", self.credit_card.card_type(639987465855678))

    def test_thatWhenDigitAreInputted_andLengthIsValid_andTheFirstDigitIs3_andSecondDigitIs7_cardTypeIsAmericanExpress(self):
        self.assertEqual("American Express Card", self.credit_card.card_type(379987465855678))

    def test_thatWhenDigitsAreInputted_iGetAnArrayOfTheDigits(self):
        self.assertEqual([1, 2, 3, 4, 5], self.credit_card.get_array_of(12345))

    def test_thatWhenDigitsAreInputted_iGetAnArrayOfTheDigits_withTheSecondDigitsDoubled_fromRightToLeft(self):
        self.assertEqual([2, 2, 6, 4, 10, 6], self.credit_card.double_second_elements_right_to_left(123456))

    def test_thatWhenDigitsAreInputted_iGetAnArrayOfTheDigits_withTheSecondDigitsDoubled_fromRightToLeft_withoutAnyDoubleDigit(self):
        self.assertEqual([2, 2, 6, 4, 1, 6], self.credit_card.double_second_elements_right_to_left_no_double_digit(123456))

    def test_thatWhenDigitAreInputted_iGetTheSumOfTheSecondDigits_fromRightToLeft_withoutAnyDoubleDigit(self):
        self.assertEqual(9, self.credit_card.sum_of_second_digits_right_to_left(123456))

    def test_thatWhenDigitAreInputted_iGetTheSumOfTheOddPlacedDigits_fromRightToLeft(self):
        self.assertEqual(12, self.credit_card.sum_of_odd_placed_digits_right_to_left(123456))

    def test_thatWhenDigitsAreInputted_iGetTheSumOfOddPlacedAndSecondDigits(self):
        self.assertEqual(21, self.credit_card.sum_of_odd_placed_second_digits_right_to_left(123456))

    def test_thatWhenDigitsAreInputted_ifSumIsDivisibleByTen_cardIsValid(self):
        self.assertTrue(self.credit_card.is_card_valid(5399831619690403))
