## STARTER CODE
file = open('2016/Day19_data.txt', 'r')

# PART 1

elves = int(file.read())

presents = {elf: 1 for elf in range(1, elves + 1)}
curr, next = 1, 2
while True:
    next = curr % elves + 1
    while presents[next] == 0:
        next = next % elves + 1

    presents[curr] += presents[next]
    presents[next] = 0

    if presents[curr] == elves:
        break
    
    curr = next % elves + 1
    while presents[curr] == 0:
        curr = curr % elves + 1

print(f"Part 1: {curr}")

# PART 2

i = 1
while i * 3 < elves:
    i *= 3

print(f"Part 2: {elves - i}")