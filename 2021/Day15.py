## STARTER CODE
file = open('2021/Day15_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import deque

rows, cols = len(lines), len(lines[0])
cave = [list(map(int, lines[i])) for i in range(rows)]
dp = [[float('inf')] * rows for _ in range(cols)]
dp[0][0] = 0

q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    score = dp[r][c]
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r+dr, c+dc
        if nr in range(rows) and nc in range(cols):
            next = cave[nr][nc] + score
            if next < dp[nr][nc]:
                dp[nr][nc] = next
                q.append((nr, nc))

print(f"Part 1: {dp[rows-1][cols-1]}")

# PART 2

rows, cols = len(lines)*5, len(lines[0])*5

cave = [[] for _ in range(cols)]
for c in range(5):
    for r in range(rows):
        curr = [(j+c+(r//len(lines))) if (j+c+(r//len(lines))) <= 9 else (j+c+(r//len(lines))) % 10 + 1 for j in list(map(int, lines[r%len(lines)]))]
        cave[r].extend(curr)

dp = [[float('inf')] * rows for _ in range(cols)]
dp[0][0] = 0
q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    score = dp[r][c]
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r+dr, c+dc
        if nr in range(rows) and nc in range(cols):
            next = cave[nr][nc] + score
            if next < dp[nr][nc]:
                dp[nr][nc] = next
                q.append((nr, nc))

print(f"Part 2: {dp[rows-1][cols-1]}")