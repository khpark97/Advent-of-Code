## STARTER CODE
file = open('2015/Day19_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import defaultdict

replacements = defaultdict(list)
i = 0
while lines[i]:
    m, r = lines[i].split(' => ')
    replacements[m].append(r)
    i += 1

distinct = set()
molecule = lines[-1]

for j in range(len(molecule)):
    check = [molecule[j]]
    if j < len(molecule)-1:
        check.append(molecule[j:j+2])
    for c in check:
        if c in replacements:
            for r in replacements[c]:
                distinct.add(''.join([molecule[:j], r, molecule[j+len(c):]]).strip())    

print(f"Part 1: {len(distinct)}")

# PART 2

from collections import deque
import re

def replace(c, seq, replace):
    uniques = []
    for i in range(len(c) - len(seq)):
        if c[i:i+len(seq)] == seq:
            uniques.append(''.join([c[:i], replace, c[i+len(seq):]]))
    return uniques

def dfs():
    q = deque([(0, molecule)])
    seen = set([molecule])
    while q:
        steps, curr = q.popleft()
        for r, seqs in replacements.items():
            for s in seqs:
                if s in curr:
                    for replaced in replace(curr, s, r):
                        if replaced == 'e':
                            return steps
                        if replaced not in seen:
                            q.appendleft((steps + 1, replaced))
        if len(curr)<25:
            print(curr)
            break
    return -1

print(f"Part 2: {dfs()}")