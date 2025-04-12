## STARTER CODE
file = open('2016/Day24_data.txt', 'r')
data = file.read()
grid = data.splitlines()

# PART 1

locations = {}
for r in range(1, len(grid)-1):
    for c in range(1, len(grid[0])-1):
        if grid[r][c].isdigit():
            locations[grid[r][c]] = (r, c)

from collections import deque
def dfs(start, locs):
    q = deque([(0, start)])
    seen = set([start])
    dists = {}
    while q:
        steps, curr = q.popleft()
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = tuple(map(sum, zip(curr, dir)))
            if nr in range(len(grid)) and nc in range(len(grid[0])):
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    next = grid[nr][nc]
                    if next == '#':
                        continue
                    elif next in locs:
                        dists[next] = steps + 1
                        if len(dists) == len(locs):
                            return dists
                    q.append((steps + 1, (nr, nc)))

routes = {}
for loc in locations:
    destinations = {k:v for k, v in locations.items() if k != loc}
    routes[loc] = dfs(locations[loc], destinations)

marks = locations.keys() - '0'
from itertools import permutations

shortest_p1 = float('inf')
shortest_p2 = float('inf')
for p in permutations(marks):
    order = ['0']
    order += p
    dist = 0
    for i in range(len(order) - 1):
        start, end = order[i], order[i+1]
        dist += routes[start][end]
    shortest_p1 = min(dist, shortest_p1)
    shortest_p2 = min(dist + routes[end]['0'], shortest_p2)

print(f"Part 1: {shortest_p1}")

# PART 2

print(f"Part 2: {shortest_p2}")