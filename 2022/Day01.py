## STARTER CODE
file = open('2022/Day01_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
i = 0
elves = []
elf = 0
while i < len(lines):
    if lines[i] == '':
        elves.append(elf)
        elf = 0
    else:
        elf += int(lines[i])
    i += 1

print(f"Part 1: {max(elves)}")

# PART 2
import heapq

print(f"Part 2: {sum(heapq.nlargest(3, elves))}")