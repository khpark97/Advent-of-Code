## STARTER CODE
file = open('2021/Day09_data.txt', 'r')
data = file.read()
field = data.splitlines()

# PART 1

basins = []
score = 0
for r in range(len(field)):
    for c in range(len(field[0])):
        curr = int(field[r][c])
        low = 0
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = tuple(map(sum, zip((r, c), d)))
            if nr not in range(len(field)) or nc not in range(len(field[0])):
                low += 1
            elif int(field[nr][nc]) > curr:
                low += 1
        if low == 4:
            score += curr + 1
            basins.append((r, c))

print(f"Part 1: {score}")

# PART 2

from collections import deque
import heapq, math

def bfs(basin):
    seen = set()
    q = deque([basin])
    while q:
        curr = q.popleft()
        seen.add(curr)
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = tuple(map(sum, zip(curr, d)))
            if nr in range(len(field)) and nc in range(len(field[0])) and (nr, nc) not in seen:
                if field[nr][nc] != '9':
                    q.append((nr, nc))
                    seen.add((nr, nc))
    return len(seen)

sizes = []
for b in basins:
    sizes.append(bfs(b))

score = 1
score *= math.prod(heapq.nlargest(3, sizes))

print(f"Part 2: {score}")