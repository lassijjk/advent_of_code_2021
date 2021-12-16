
file1 = open("input.txt", "r")
lines = file1.readlines()
file1.close()
lines = [line[:-1] for line in lines]

# Task 1
x, y = 0, 0
for line in lines:
    parts = line.split()
    if parts[0] == 'forward':
        x += int(parts[1])
    elif parts[0] == 'up':
        y -= int(parts[1])
    else:
        y += int(parts[1])

print(x, y, x*y)

# Task 2
x, y, aim = 0, 0, 0
for line in lines:
    [command, value] = line.split()
    value = int(value)
    if command == 'forward':
        x += value
        y += aim*value
    elif command == 'up':
        aim -= value
    else:
        aim += value

print(x, y, x*y)
