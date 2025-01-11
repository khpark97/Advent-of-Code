## STARTER CODE
file = open('Day16_data', 'r')
data = file.read()
lines = data.splitlines()

import heapq
from collections import defaultdict

# PART 1
start, end = (), ()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'S':
            start = (r, c)
        elif lines[r][c] == 'E':
            end = (r, c)

score = 0
q, seen = [], set()
q.append([0, start, 0])
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while q:
    # print(q)
    score, curr, d = heapq.heappop(q)
    seen.add(curr)
    for dir in range(len(dirs)):
        r, c = tuple(map(sum, zip(curr, dirs[dir])))
        if (r, c) not in seen:
            next = lines[r][c]
            if next == 'E':
                score += 1
                q.clear()
            elif next == '.':
                if d == dir:
                    heapq.heappush(q, [score+1, (r, c), d])
                else:
                    heapq.heappush(q, [score+1001, (r, c), dir])
print(f"Part 1: {score}")

# PART 2
score = 0
q, seen = [], defaultdict(int)
q.append([0, start, 0, set()])
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
tiles = set([start])
high = float("inf")

while q:
    # print(q)
    score, curr, d, path_old = heapq.heappop(q)
    seen[curr] = min(score, seen[curr])
    path_old.add(curr)
    if score > high:
        continue
    for change in [-1, 0, 1]:
        path = path_old.copy()
        dir = (d+change)%4
        r, c = tuple(map(sum, zip(curr, dirs[dir])))
        if (r, c) in seen and seen[(r, c)] + 1001 > score:
            continue
        next = lines[r][c]
        if next == 'E':
            high = min(high, score+1)
            path.add((r, c))
            tiles.update(path)
            # print(sorted(tiles))
        elif next == '.':
            if d == dir:
                path.add((r, c))
                heapq.heappush(q, [score+1, (r, c), d, path])
            else:
                heapq.heappush(q, [score+1000, curr, dir, path])
                
print(f"Part 2: {len(tiles)}")