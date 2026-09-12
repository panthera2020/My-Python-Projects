class CardValidation:

    def is_length_valid(self, card_number):
        return 13 <= self.get_length(card_number) <= 16

    def get_length(self, card_number):
        counter = 0
        while card_number != 0:
            counter += 1
            card_number = card_number // 10
        return counter

    def is_first_digit_valid(self, card_number):
        card_string = str(card_number)
        first_digit = card_string[0]
        second_digit = card_string[1]
        return first_digit in ['4', '5', '6'] or (first_digit == '3' and second_digit == '7')

    def card_type(self, card_number):
        card_string = str(card_number)
        first_digit = card_string[0]
        second_digit = card_string[1]

        if first_digit == '4':
            return "Visa"
        elif first_digit == '5':
            return "MasterCard"
        elif first_digit == '6':
            return "Discover Card"
        elif first_digit == '3' and second_digit == '7':
            return "American Express Card"
        return "Unknown"

    def get_array_of(self, numbers):
        return [int(digit) for digit in str(numbers)]

    def double_second_elements_right_to_left(self, numbers):
        array = self.get_array_of(numbers)
        for index in range(len(array) - 2, -1, -2):
            array[index] = array[index] * 2
        return array

    def double_second_elements_right_to_left_no_double_digit(self, numbers):
        array = self.double_second_elements_right_to_left(numbers)
        for index in range(len(array) - 2, -1, -2):
            if array[index] > 9:
                array[index] = sum(int(digit) for digit in str(array[index]))
        return array

    def sum_of_second_digits_right_to_left(self, numbers):
        array = self.double_second_elements_right_to_left_no_double_digit(numbers)
        return sum(array[index] for index in range(len(array) - 2, -1, -2))

    def sum_of_odd_placed_digits_right_to_left(self, numbers):
        array = self.get_array_of(numbers)
        return sum(array[index] for index in range(len(array) - 1, -1, -2))

    def sum_of_odd_placed_second_digits_right_to_left(self, numbers):
        return self.sum_of_odd_placed_digits_right_to_left(numbers) + self.sum_of_second_digits_right_to_left(numbers)

    def is_card_valid(self, numbers):
        return self.sum_of_odd_placed_second_digits_right_to_left(numbers) % 10 == 0