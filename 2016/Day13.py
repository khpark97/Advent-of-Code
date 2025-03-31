## STARTER CODE
file = open('2016/Day13_data.txt', 'r')

# PART 1

favorite = int(file.read())
def wall(x, y):
    curr = x*x + 3*x + 2*x*y + y + y*y
    curr += favorite
    binary = bin(curr)[2:]
    if binary.count('1') % 2 == 0:
        return '.'
    return '#'
    
from collections import deque
def bfs_p1(start, end):
    q = deque([(start, 0)])
    seen = set([start])
    while q:
        curr, score = q.popleft()
        seen.add(curr)
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next = tuple(map(sum, zip(curr, dir)))
            if any([n < 0 for n in next]):
                continue
            if next not in seen:
                if next == end:
                    return score + 1
                if wall(*next) == '#':
                    seen.add(next)
                else:
                    q.append((next, score + 1))

print(f"Part 1: {bfs_p1((1, 1), (31, 39))}")

# PART 2

def bfs_p2(start, end):
    q = deque([(start, 0)])
    path = set([start])
    bad = set([start])
    while q:
        curr, score = q.popleft()
        path.add(curr)
        if score == end:
            continue
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next = tuple(map(sum, zip(curr, dir)))
            if any([n < 0 for n in next]):
                continue
            if next not in bad:
                bad.add(next)
                if wall(*next) != '#':
                    q.append((next, score + 1))
    return len(path)

print(f"Part 2: {bfs_p2((1, 1), 50)}")