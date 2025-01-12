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

def maze():
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
    return low

print(f"Part 1: {maze()}")

# PART 2
cutoff = 1024
while maze() != float("inf"):
    x, y = map(int, lines[cutoff].split(','))
    board[y] = board[y][:x] + '#' + board[y][x+1:]
    cutoff += 1

print(f"Part 2: {x},{y}")