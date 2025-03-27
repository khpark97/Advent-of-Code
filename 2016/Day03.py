## STARTER CODE
file = open('2016/Day03_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import heapq

valid_p1 = 0
for l in lines:
    sides = [int(x) for x in l.split()]
    if sum(heapq.nsmallest(2, sides)) > max(sides):
        valid_p1 += 1

print(f"Part 1: {valid_p1}")

# PART 2

valid_p2 = 0
i = 0
while i < len(lines):
    triangles = []
    for j in range(i, i+3):
        triangles.append([int(x) for x in lines[j].split()])
    triangles = list(zip(*triangles))
    for t in triangles:
        if sum(heapq.nsmallest(2, t)) > max(t):
            valid_p2 += 1
    i += 3

print(f"Part 2: {valid_p2}")