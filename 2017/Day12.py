## STARTER CODE
file = open('2017/Day12_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
connections = {}
for line in lines:
    program, *connected = [int(x) for x in re.findall(r'\d+', line)]
    connections[program] = connected

from collections import deque
def find_group(id):
    q = deque([id])
    seen = set([id])
    while q:
        curr = q.popleft()
        for connected in connections[curr]:
            if connected not in seen:
                seen.add(connected)
                q.append(connected)
    return seen

group = find_group(0)

print(f"Part 1: {len(group)}")

# PART 2

groups = 1
for c in connections:
    if c not in group:
        group.update(find_group(c))
        groups += 1

print(f"Part 2: {groups}")