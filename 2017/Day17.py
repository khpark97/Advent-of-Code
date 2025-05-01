## STARTER CODE
file = open('2017/Day17_data.txt', 'r')
steps = int(file.read())

# PART 1

buffer = [0]
position = 0
for i in range(1, 2018):
    position = (position + steps) % i + 1
    buffer = buffer[:position] + [i] + buffer[position:]

print(f"Part 1: {buffer[position+1]}")

# PART 2

position = 0
after_zero = 0
for i in range(1, 50000001):
    position = (position + steps) % i + 1
    if position == 1:
        after_zero = i

print(f"Part 2: {after_zero}")