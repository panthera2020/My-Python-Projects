from functools import reduce


class reduce_one:
    def multiply(self,accumulator, number):
        return number * accumulator

    def get_product(self, numbers):
        return reduce(self.multiply, numbers)

class reduce_two:
    def get_max(self,accumulator, number):
        if number > accumulator:
            return number
        else:
            return accumulator

    def get_maximum_value(self, numbers):
        return reduce(self.get_max, numbers)

class reduce_three:
    def add_word(self, accumulator, word):
        return accumulator + word

    def concatenate(self, words):
        return reduce(self.add_word, words)

class reduce_four:
    def get_square(self, accumulator, number):
        return  accumulator + (number ** 2)

    def sum_of_squares(self, numbers):
        return reduce(self.get_square, numbers)

class reduce_five:

    def add_dictonary(self, accumulator, dictionary):
        return {list(accumulator.keys())[0] + list(dictionary.keys())[0] : list(accumulator.values())[0] + list(dictionary.values())[0] }

    def compress(self, list_of_dictionaries):
        return reduce(self.add_dictonary, list_of_dictionaries)