from operator import contains


class SneakySeven:

    def get_numbers_divisible_by_seven_in(self, number):
        return [each_number for each_number in range(1, number + 1) if each_number % 7 == 0]

    def contains_seven(self, number):
        return "7" in str(number)

    def get_numbers_that_contains_seven_in(self, number):
        return [each_number for each_number in range(1, number + 1) if self.contains_seven(each_number)]

    def is_divisible_by_seven_and_contains_seven_in(self, number):
        if number % 7 == 0 and self.contains_seven(number): return False
        return True

    def get_numbers_that_contains_seven_and_divisible_by_seven_in(self, number):
        numbers_divisible_by_seven = self.get_numbers_divisible_by_seven_in(number)
        number_that_contains_seven = self.get_numbers_that_contains_seven_in(number)
        for every_number in number_that_contains_seven:
            if every_number not in numbers_divisible_by_seven: numbers_divisible_by_seven.append(every_number)
        return numbers_divisible_by_seven

    def get_numbers_that_contains_seven_and_divisible_by_seven_not_both_in(self, number):
        return  list(filter(self.is_divisible_by_seven_and_contains_seven_in, self.get_numbers_that_contains_seven_and_divisible_by_seven_in(number)))

    def count_sneaky_seven(self, number):
        return len(self.get_numbers_that_contains_seven_and_divisible_by_seven_not_both_in(number))




