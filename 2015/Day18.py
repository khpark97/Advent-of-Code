## STARTER CODE
file = open('2015/Day18_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re

lights_p1 = [line for line in lines]
rows, cols = len(lights_p1), len(lights_p1[0])

def toggle(config, part):
    step = []
    for r in range(rows):
        row = []
        for c in range(cols):
            #logic to have each corner stay on for part 2
            if part == '2':
                if ((r == 0 and c == 0) or
                    (r == rows-1 and c == 0) or
                    (r == 0 and c == cols-1) or
                    (r == rows-1 and c == cols-1)):
                    row.append('#')
                    continue

            curr = config[r][c]
            neis = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = tuple(map(sum, zip((r, c), (dr, dc))))
                if nr in range(rows) and nc in range(cols):
                    if config[nr][nc] == '#':
                        neis += 1
            if curr == '#' and neis in [2, 3]:
                row.append('#')
            elif curr == '.' and neis == 3:
                row.append('#')
            else:
                row.append('.')
        step.append(''.join(row))
    return step

for _ in range(100):
    lights_p1 = toggle(lights_p1, '1')

total_p1 = 0
for r in lights_p1:
    total_p1 += len(re.findall('#', r))

print(f"Part 1: {total_p1}")

# PART 2

lights_p2 = [line for line in lines]
lights_p2[0] = '#' + lights_p2[0][1:-1] + '#'
lights_p2[-1] = '#' + lights_p2[-1][1:-1] + '#'

for _ in range(100):
    lights_p2 = toggle(lights_p2, '2')

total_p2 = 0
for r in lights_p2:
    total_p2 += len(re.findall('#', r))

print(f"Part 2: {total_p2}")