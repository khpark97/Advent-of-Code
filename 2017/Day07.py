## STARTER CODE
file = open('2017/Day07_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
parents = {}
programs = []
for l in lines:
    split = l.split()
    name = split[0]
    programs.append(name)
    if '->' in split:
        above = [p.strip(',') for p in split[split.index('->') + 1:]]
        for a in above:
            parents[a] = name

print(f"Part 1: {(programs - parents.keys()).pop()}")

# PART 2

from collections import deque, Counter

q = deque(lines)
weights = {}
fix = -1
while q:
    curr = q.popleft()
    split = curr.split()
    name = split[0]
    weight = [int(x) for x in re.findall(r'\d+', curr)][0]
    if '->' in split:
        above = [p.strip(',') for p in split[split.index('->') + 1:]]
        if not all([a in weights for a in above]):
            q.append(curr)
        else:
            if not all(sum(weights[a]) == sum(weights[above[0]]) for a in above[1:]):
                counter = Counter()
                tower = {}
                for a in above:
                    total = sum(weights[a])
                    tower[total] = a
                    counter.update([sum(weights[a])])
                most = counter.popitem()
                least = counter.popitem()
                diff = most[0] - least[0]
                fix = weights[tower[least[0]]][0] + diff
                break
                    
            disc = sum([sum(weights[a]) for a in above])
            weights[name] = [weight, disc]
        continue
    weights[name] = [weight]

print(f"Part 2: {fix}")