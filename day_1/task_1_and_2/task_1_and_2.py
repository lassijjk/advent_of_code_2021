
# Reading the file into a list using readlines
file1 = open("input.txt", "r")
lines = file1.readlines()
file1.close()

# Removing newlines from each line using list comprehension
numbers = [int(line[:-1]) for line in lines]

# Initial parameters for the loop
old_number = 0
increasing = -1

# For loop using sum(list) to calculate values of each window
for i in range(len(lines)-2):
    number = sum(numbers[i:i+3])
    if number > old_number:
        increasing += 1
    old_number = number

print(increasing)

# Task 1 was the same loop but instead of 'for i in range()' I used for line in lines
