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

lowest = score

paths = []
start, end = (), ()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'S':
            start = (r, c)
        elif lines[r][c] == 'E':
            end = (r, c)
        elif lines[r][c] == '.':
            paths.append((r, c))

from_start = {p: float('inf') for p in paths}
from_start[start] = 0
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
            if next == '.':
                if d == dir:
                    if score + 1 < from_start[(r, c)]:
                        from_start[(r, c)] = score + 1
                    heapq.heappush(q, [score+1, (r, c), d])
                else:
                    if score + 1001 < from_start[(r, c)]:
                        from_start[(r, c)] = score + 1001
                    heapq.heappush(q, [score+1001, (r, c), dir])

path = set(end)
from_end = {p: float('inf') for p in paths}
from_end[start] = 0
score = 0
q, seen = [], set()
q.append([0, end, 0])
q.append([0, end, 1])
q.append([0, end, 2])
q.append([0, end, 3])
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while q:
    # print(q)
    score, curr, d = heapq.heappop(q)
    seen.add(curr)
    for dir in range(len(dirs)):
        r, c = tuple(map(sum, zip(curr, dirs[dir])))
        if (r, c) not in seen:
            next = lines[r][c]
            if next == '.':
                if d == dir:
                    if score + 1 < from_end[(r, c)]:
                        from_end[(r, c)] = score + 1
                    heapq.heappush(q, [score+1, (r, c), d])
                else:
                    if score + 1001 < from_end[(r, c)]:
                        from_end[(r, c)] = score + 1001
                    heapq.heappush(q, [score+1001, (r, c), dir])

print(f"Part 2: {len(path)}")