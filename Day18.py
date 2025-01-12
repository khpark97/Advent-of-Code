## STARTER CODE
file = open('Day18_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
size = 71
board = ['.'*size for i in range(size)]
for byte in lines[:1024]:
    x, y = map(int, byte.split(','))
    board[y] = board[y][:x] + '#' + board[y][x+1:]

# for l in board:
#     print(l)

q, seen = deque(), set()
q.append([1, (0, 0)])
seen.add((0, 0))
low = float("inf")
while q:
    # print(q)
    score, pos = q.popleft()
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = tuple(map(sum, zip(pos, dir)))
        if (r, c) == (size-1, size-1):
            low = min(low, score)
            q.clear()
        elif r in range(size) and c in range(size) and (r, c) not in seen:
            next = board[r][c]
            if next == '.':
                q.append([score+1, (r, c)])
                seen.add((r, c))

print(f"Part 1: {low}")

# PART 2
def maze():
    q, seen = deque(), set()
    path = set([(0, 0)])
    q.append([1, (0, 0), path])
    seen.add((0, 0))
    while q:
        # print(q)
        score, pos, path = q.popleft()
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = tuple(map(sum, zip(pos, dir)))
            if (r, c) == (size-1, size-1):
                path.add((r, c))
                q.clear()
            elif r in range(size) and c in range(size) and (r, c) not in seen:
                next = board[r][c]
                copy = path.copy()
                copy.add((r, c))
                if next == '.':
                    q.append([score+1, (r, c), copy])
                    seen.add((r, c))
    return path

cutoff = 1024
path = maze()
while True:
    x, y = map(int, lines[cutoff].split(','))
    board[y] = board[y][:x] + '#' + board[y][x+1:]
    if (y, x) in path:
        path = maze()
    cutoff += 1
    if (70, 70) not in path:
        break

print(f"Part 2: {x},{y}")