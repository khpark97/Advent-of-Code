## STARTER CODE
file = open('Day8_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict
from itertools import combinations

# PART 1
symbols = defaultdict(list)
for r in range(len(lines)):
    for c in range(len(lines[0])):
        sym = lines[r][c]
        if sym != '.':
            symbols[sym].append([r, c])

def antinode(combo):
    c1, c2 = combo
    r1 = [c1[0] - (c2[0]-c1[0]), c1[1] - (c2[1]-c1[1])]
    r2 = [c2[0] + (c2[0]-c1[0]), c2[1] + (c2[1]-c1[1])]
    return r1, r2

total = 0
seen = set()
for symbol in symbols:
    coords = symbols[symbol]
    for c in combinations(coords, 2):
        nodes = antinode(c)
        for node in nodes:
            if node[0] in range(0, len(lines)) and node[1] in range(0, len(lines[0])) and (node[0], node[1]) not in seen:
                total += 1
                seen.add((node[0], node[1]))
print(total)

# PART 2
symbols = defaultdict(list)
for r in range(len(lines)):
    for c in range(len(lines[0])):
        sym = lines[r][c]
        if sym != '.':
            symbols[sym].append([r, c])

seen = set()
total = 0

def find_antinodes(combo):
    r1, r2 = [list(l) for l in combo]
    diff1, diff2 = r2[0] - r1[0], r2[1] - r1[1]
    res = 0
    while r1[0] in range(0, len(lines)) and r1[1] in range(0, len(lines[0])):
        if (r1[0], r1[1]) not in seen:
            res += 1
            seen.add((r1[0], r1[1]))
        r1[0] -= diff1
        r1[1] -= diff2
    while r2[0] in range(0, len(lines)) and r2[1] in range(0, len(lines[0])):
        if (r2[0], r2[1]) not in seen:
            res += 1
            seen.add((r2[0], r2[1]))
        r2[0] += diff1
        r2[1] += diff2
    return res

for symbol in symbols:
    coords = symbols[symbol]
    for c in combinations(coords, 2):
        nodes = find_antinodes(c)
        total += nodes
print(total)