## STARTER CODE
file = open('2015/Day20_data.txt', 'r')
data = file.read()

# PART 1

import math

presents = int(data)
houses_p1 = [0 for _ in range(presents//10 + 1)]
houses_p2 = [0 for _ in range(presents//10 + 1)]

for i in range(1, presents//10 + 1):
    for j in range(i, presents//10 + 1, i):
        houses_p1[j] += i * 10
    for k in range(i, min(presents//10 + 1, i * 50 + 1) , i):
        houses_p2[k] += i * 11

p1 = [h for h, house in enumerate(houses_p1) if house > presents][0]

print(f"Part 1: {p1}")

# PART 2

p2 = [h for h, house in enumerate(houses_p2) if house > presents][0]

print(f"Part 2: {p2}")