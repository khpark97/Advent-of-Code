## STARTER CODE
file = open('2016/Day20_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
ranges = [(int(start), int(end)) for start, end in [re.findall(r'\d+', l) for l in lines]]

curr, lowest = 0, float('inf')
allowed = 0
for r in sorted(ranges):
    start, end = r
    if curr >= start:
        curr = max(curr, end + 1)
    else:
        lowest = min(lowest, curr)
        allowed += start - curr
        curr = end + 1

print(f"Part 1: {lowest}")

# PART 2

print(f"Part 2: {allowed}")