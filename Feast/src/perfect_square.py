import math

class perfect_square:

    def is_perfect_number(self, number):
        return math.sqrt(number) % 1 == 0

    def check_perfect_squares(self, numbers):
        return [self.is_perfect_number(number) for number in numbers]

