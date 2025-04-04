## STARTER CODE
file = open('2016/Day17_data.txt', 'r')

# PART 1

passcode = file.read()

from collections import deque
import hashlib

rows, cols = 4, 4
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir_chars = ['U', 'D', 'L', 'R']
def dfs():
    valid = []
    q = deque([((0, 0), [])])
    while q:
        curr, path = q.popleft()
        if curr == (rows-1, cols-1):
            valid.append((len(path), ''.join(path)))
            continue
        key = f"{passcode}{''.join(path)}"
        hex = hashlib.md5(key.encode('utf-8')).hexdigest()
        doors = [(i, val) for i, val in enumerate(hex[:4])]
        for i, val in doors:
            path_copy = path.copy()
            if val in ['b', 'c', 'd', 'e', 'f']:
                nr, nc = tuple(map(sum, zip(curr, dirs[i])))
                if nr in range(rows) and nc in range(cols):
                    path_copy.append(dir_chars[i])
                    q.append(((nr, nc), path_copy))
    return valid

search = dfs()

print(f"Part 1: {min(search)[1]}")

# PART 2

print(f"Part 2: {max(search)[0]}")