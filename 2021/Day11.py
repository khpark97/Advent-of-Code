## STARTER CODE
file = open('2021/Day11_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
from collections import deque

octopuses = []
for l in lines:
    octopuses.append(list(map(int, l)))

score = 0
def step():
    total = 0
    q = deque()
    seen = set()
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            octopuses[r][c] += 1
            if octopuses[r][c] > 9:
                q.append((r, c))
                seen.add((r, c))
    
    while q:
        flash = q.popleft()
        for adj in [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]:
            nr, nc = tuple(map(sum, zip(flash, adj)))
            if nr in range(len(octopuses)) and nc in range(len(octopuses[0])) and (nr, nc) not in seen:
                octopuses[nr][nc] += 1
                if octopuses[nr][nc] > 9:
                    q.append((nr, nc))
                    seen.add((nr, nc))

    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            if octopuses[r][c] > 9:
                total += 1
                octopuses[r][c] = 0

    if total == 100:
        return -1
    return total

i = 0
flash = 0
while flash != -1:
    flash = step()
    if i < 100:
        score += flash
    i += 1

print(f"Part 1: {score}")

# PART 2

print(f"Part 2: {i}")