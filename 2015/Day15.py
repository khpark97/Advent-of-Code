## STARTER CODE
file = open('2015/Day15_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
from math import prod

ingredients = {}
for l in lines:
    ingredients[l.split()[0]] = [int(x) for x in re.findall(r'-?\d+', l)]

def calculate(teaspoons, part):
    properties = [0 for _ in range(5)]
    for i, ing in enumerate(ingredients):
        for j in range(len(ingredients[ing])):
            properties[j] += ingredients[ing][j] * teaspoons[i]
    score = prod([p if p > 0 else 0 for p in properties][:4])
    if part == 'a':
        return score
    if part == 'b':
        return score if properties[4] == 500 else 0

p1, p2 = 0, 0
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            l = 100 - i - j - k
            p1 = max(p1, calculate([i, j, k, l], 'a'))
            p2 = max(p2, calculate([i, j, k, l], 'b'))

print(f"Part 1: {p1}")

# PART 2

print(f"Part 2: {p2}")