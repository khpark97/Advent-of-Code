## STARTER CODE
file = open('2021/Day02_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

x, y = 0, 0
for line in lines:
    command, value = line.split()
    value = int(value)
    match command:
        case 'forward': x += value
        case 'up': y -= value
        case 'down': y += value

print(f"Part 1: {x * y}")

# PART 2

x, y, aim = 0, 0, 0
for line in lines:
    command, value = line.split()
    value = int(value)
    match command:
        case 'forward': 
            x += value
            y += aim * value
        case 'up': aim -= value
        case 'down': aim += value

print(f"Part 2: {x * y}")