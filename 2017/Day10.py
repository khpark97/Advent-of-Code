## STARTER CODE
file = open('2017/Day10_data.txt', 'r')
data = file.read()

# PART 1

import re
lengths = [int(x) for x in re.findall(r'\d+', data)]

elements = [e for e in range(256)]

pos, skip = 0, 0
for l in lengths:
    leftovers = 0
    curr = elements[pos:min(pos+l, len(elements))]
    if pos + l > len(elements):
        # Loops back around to the elements in the front
        leftovers = (pos + l) % len(elements)
        curr += elements[:leftovers]

    curr.reverse()
    for i in range(pos, min(pos+l, len(elements))):
        elements[i] = curr[i - pos]
        
    i += 1
    for j in range(leftovers):
        elements[j] = curr[(i - pos) + j]

    pos = (pos + l + skip) % len(elements)
    skip += 1

score = 0
print(f"Part 1: {elements[0] * elements[1]}")

# PART 2

print(f"Part 2: {score}")