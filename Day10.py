## STARTER CODE
file = open('Day10_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
starts = []
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == '0':
            starts.append((r, c))

def trail(r, c):
    seen = set([(r, c)])
    path = deque([(r, c)])
    curr = 0
    while path:
        for i in range(len(path)):
            r, c = path.popleft()
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if r+dr in range(len(lines)) and c+dc in range(len(lines[0])):
                    next = int(lines[r+dr][c+dc])
                    if next == curr + 1 and (r+dr, c+dc) not in seen:
                        path.append((r+dr, c+dc))
                        seen.add((r+dr, c+dc))
        curr += 1
        if curr == 9:
            return len(path)

total = 0
for r, c in starts:
    total += trail(r, c)

print(f"Part 1: {total}")

# PART 2
def trail(r, c):
    path = deque([(r, c)])
    curr = 0
    while path:
        for i in range(len(path)):
            r, c = path.popleft()
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if r+dr in range(len(lines)) and c+dc in range(len(lines[0])):
                    next = int(lines[r+dr][c+dc])
                    if next == curr + 1:
                        path.append((r+dr, c+dc))
        curr += 1
        if curr == 9:
            return len(path)

total = 0
for r, c in starts:
    total += trail(r, c)

print(f"Part 2: {total}")