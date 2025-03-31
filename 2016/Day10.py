## STARTER CODE
file = open('2016/Day10_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import defaultdict, deque
import re
bots = defaultdict(list)
values = [l for l in lines if l.split()[0] == 'value']
for v in values:
    chip, bot = [int(x) for x in re.findall(r"\d+", v)]
    bots[bot].append(chip)

part_1 = 0

output = defaultdict(int)
commands = [l for l in lines if l.split()[0] == 'bot']
q = deque(commands)

while q:
    curr = q.popleft()
    bot, first, second = [int(x) for x in re.findall(r"\d+", curr)]
    if len(bots[bot]) != 2:
        q.append(curr)
        continue
    if sorted(bots[bot]) == [17, 61]:
        part_1 = bot
    split = curr.split()
    if split[5] == 'bot':
        bots[first].append(min(bots[bot]))
    elif split[5] == 'output':
        output[first] = min(bots[bot])
    if split[10] == 'bot':
        bots[second].append(max(bots[bot]))
    elif split[10] == 'output':
        output[second] = max(bots[bot])
    # bots[bot] = []
    
print(f"Part 1: {part_1}")

# PART 2

import math
print(f"Part 2: {math.prod([output[i] for i in range(3)])}")