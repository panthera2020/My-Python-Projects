
numbers = []
count = 0

for _ in range(2):
    each_number =[]
    for _ in range(3):
        each_number.append(count)
        count += 1
    numbers.append(each_number)

print(numbers)
print()

print(f'{"":>5} {"Column 1":>5} {"Column 2":>5} {"Column 3":>5}')
print(f'{"Row 1":>5} {numbers[0][0]:>8} {numbers[0][1]:>8} {numbers[0][2]:>8}')
print(f'{"Row 2":>5} {numbers[1][0]:>8} {numbers[1][1]:>8} {numbers[1][2]:>8}')