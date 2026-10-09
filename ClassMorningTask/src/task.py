

def digit_sum_number_until_single_digit(number):
    sum = 0
    while True:
        digit = number % 10
        sum += digit
        number //= 10
        if number == 0 and sum > 9:
            number = sum
            sum = 0
        elif number == 0 and sum < 10:
            return sum

