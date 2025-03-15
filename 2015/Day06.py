## STARTER CODE
file = open('2015/Day06_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for l in lines:
    s0, s1, e0, e1 = [int(x) for x in re.findall(r'\d+', l)]
    for r in range(s0, e0 + 1):
        for c in range(s1, e1 + 1):
            if l.split()[0] == 'toggle':
                lights[r][c] = 1 - lights[r][c]
            else:
                lights[r][c] = (1 if l.split()[1] == 'on' else 0)

total = sum([sum(r) for r in lights])

print(f"Part 1: {total}")

# PART 2

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for l in lines:
    s0, s1, e0, e1 = [int(x) for x in re.findall(r'\d+', l)]
    for r in range(s0, e0 + 1):
        for c in range(s1, e1 + 1):
            if l.split()[0] == 'toggle':
                lights[r][c] += 2
            elif l.split()[1] == 'on':
                lights[r][c] += 1
            else:
                lights[r][c] = max(0, lights[r][c] - 1)

total = sum([sum(r) for r in lights])

print(f"Part 2: {total}")