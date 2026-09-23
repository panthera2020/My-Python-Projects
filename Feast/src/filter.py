
class filter_one:
    def is_digit(self, digit):
        return type(digit) == int

    def get_digits(self, elements):
        return list(filter(self.is_digit, elements))

class filter_two:

    def is_divisible_by_three(self, number):
        return number % 3 == 0

    def get_numbers_divisible_by_three(self, list_of_numbers):
        return list(filter(self.is_divisible_by_three, list_of_numbers))

class filter_three:
    def is_positive(self, number):
        return number >= 0

    def get_positive_numbers(self, list_of_numbers):
        return list(filter(self.is_positive, list_of_numbers))

class filter_four:
    def is_value_greater_than_25(self, dictionary):
        return dictionary['age'] >= 25

    def get_element_greater_than_25(self, dictionaries):
        return list(filter(self.is_value_greater_than_25, dictionaries))