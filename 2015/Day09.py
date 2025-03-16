## STARTER CODE
file = open('2015/Day09_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from itertools import permutations

edges = {}
cities = set()
for l in lines:
    c1, _, c2, _, dist = l.split()
    edges[(c1, c2)] = edges[(c2, c1)] = int(dist)
    cities.add(c1)
    cities.add(c2)

shortest = float('inf')
longest = 0
for p in permutations(cities):
    dist = 0
    for i in range(len(p) - 1):
        pair = p[i], p[i+1]
        if pair in edges:
            dist += edges[pair]
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print(f"Part 1: {shortest}")

# PART 2

print(f"Part 2: {longest}")