numbers = [5, 12, 7, 20, 3]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest =", largest)