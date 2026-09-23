
def areAllPrimes(numbers):
    prime_counter = 0
    prime_count = 0
    isAllPrime = False
    for number in numbers:
        prime_counter = 0
        for count in range(1,number + 1):
            if number % count == 0:
                prime_counter += 1
        if prime_counter == 2:
            prime_count += 1

    if(prime_count == len(numbers)):
        isAllPrime = True
    return isAllPrime

numbers_one = [2,3,5,7,11]
numbers_two = [1,2,3,4,5]

print(areAllPrimes(numbers_one))
print(areAllPrimes(numbers_two))