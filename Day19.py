## STARTER CODE
file = open('Day19_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
towels = lines[0].split(', ')
designs = lines[2:]

total = 0
for d in designs:
    q = deque()
    q.append(0)
    while q:
        pointer = q.pop()
        for t in towels:
            curr = d[pointer:]
            if curr == t:
                total += 1
                q.clear()
                break
            elif curr.startswith(t):
                q.append(pointer + len(t))

print(f"Part 1: {total}")

# PART 2
total = 0
for d in designs:
    combinations = [1]+[0]*(len(d))
    for i in range(len(combinations)):
        if combinations[i] == 0:
            continue
        for t in towels:
            curr = d[i:]
            if curr.startswith(t):
                combinations[i+len(t)] += combinations[i]
            # print(combinations)
    total += combinations[-1]

print(f"Part 2: {total}")
