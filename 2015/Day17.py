## STARTER CODE
file = open('2015/Day17_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from itertools import combinations

containers = [int(x) for x in lines]
liters = 150

p1, p2 = 0, 0
low = float('inf')
for i in range(len(containers)):
    minimum = 0
    for c in combinations(containers, i):
        if sum(c) == liters:
            low = min(low, i)
            minimum += 1
    if p2 == 0 and low != float('inf'):
        p2 = minimum
    p1 += minimum

print(f"Part 1: {p1}")

# PART 2

print(f"Part 2: {p2}")