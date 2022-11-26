# Range: used to generate a sequence of numbers
# It will start from 0, up to the number that has been specify
# It will exclude the last specific number as it always starts with 0

numbers = range(5)  # It will return a range of numbers
# It will start from 0, up to the number that has been specify
for item in numbers:
    print(item)
print(".\n")

specificRange = range(5, 10)  # It returns a specific range of numbers
# It will start from 5, up to 10
for item in specificRange:
    print(item)
print(".\n")

specificRangeWithStep = range(5, 10, 2)  # It returns a specific range of numbers and can skip certain amount of number
# It will start from 5, up to 10
for item in specificRangeWithStep:
    print(item)
