## STARTER CODE
file = open('2017/Day14_data.txt', 'r')
key = file.read()

from Day10 import knot_p2

# PART 1

inputs = [key + '-' + str(i) for i in range(128)]
grid = []
for i in inputs:
    hash = knot_p2(i)
    grid.append(f"{int(hash, 16):0128b}")

score = 0
for row in grid:
    ints = [int(bit) for bit in row]
    score += sum(ints)

print(f"Part 1: {score}")

# PART 2

from collections import deque
ones = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '1']
seen = set()
groups = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
for i in range(len(ones)):
    if ones[i] not in seen:
        q.append(ones[i])
        groups += 1
    while q:
        curr = q.popleft()
        seen.add(curr)
        for d in dirs:
            nr, nc = tuple(map(sum, zip(curr, d)))
            if nr in range(len(grid)) and nc in range(len(grid[0])):
                if (nr, nc) not in seen:
                    if grid[nr][nc] == '1':
                        q.append((nr, nc))

print(f"Part 2: {groups}")