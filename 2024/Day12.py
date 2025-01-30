## STARTER CODE
file = open('Day12_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
total = 0
seen = set()

def bfs(r, c):
    q = deque()
    a = 0
    p = 0
    q.append((r, c))
    seen.add((r, c))
    plant = lines[r][c]
    while q:
        r, c = q.popleft()
        a += 1
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if r+dr in range(len(lines)) and c+dc in range(len(lines[0])):
                nei = lines[r+dr][c+dc]
                if nei == plant:
                    if (r+dr, c+dc) not in seen:
                        seen.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))
                else:
                    p += 1
            else:
                p += 1
    return a * p

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if (r, c) not in seen:
            total += bfs(r, c)

print(f"Part 1: {total}")

# PART 2
total = 0
seen = set()

def bfs(r, c):
    q = deque()
    region = set()
    q.append((r, c))
    seen.add((r, c))
    region.add((r, c))
    plant = lines[r][c]
    while q:
        r, c = q.popleft()
        region.add((r, c))
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if r+dr in range(len(lines)) and c+dc in range(len(lines[0])):
                nei = lines[r+dr][c+dc]
                if nei == plant:
                    if (r+dr, c+dc) not in seen:
                        q.append((r+dr, c+dc))
                        seen.add((r+dr, c+dc))
    return region

regions = []
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if (r, c) not in seen:
            regions.append([lines[r][c], bfs(r, c)])

def corner(plant, cell):
    corners, adj = 0, 0
    r, c = cell
    for corner in [[[1, 0], [0, 1], [1, 1]], [[1, 0], [0, -1], [1, -1]], [[-1, 0], [0, 1], [-1, 1]], [[-1, 0], [0, -1], [-1, -1]]]:
        adj = 0
        i = 0
        while i < 3:
            if i == 2 and adj == 1:
                break
            dr, dc = corner[i]
            if r+dr in range(len(lines)) and c+dc in range(len(lines[0])):
                nei = lines[r+dr][c+dc]
                if nei == plant:
                    adj += 1
            i += 1
            if i == 3 and (adj == 1 or adj == 2):
                corners += 1
        if adj == 0:
            corners += 1
        
    return corners

total = 0
for plant, region in regions:
    sides = 0
    for cell in region:
        sides += corner(plant, cell)
    total += sides * len(region)
    # print(plant, len(region), sides, sides * len(region))

print(f"Part 2: {total}")
