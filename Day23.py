## STARTER CODE
file = open('Day23_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict

# PART 1
adj = defaultdict(list)
for x, y in [line.split('-') for line in lines]:
    adj[x].append(y)
    adj[y].append(x)
    
trios = set()
for a in adj:
    for i in adj[a]:
        for j in adj[a]:
            if j in adj[i]:
                trios.add(tuple(sorted([a, i, j])))

total = 0
for a, b, c in trios:
    if "t" in [a[0], b[0], c[0]]:
        total += 1

print(f"Part 1: {total}")

# PART 2

party = []

print(f"Part 2: {','.join(sorted(party))}")