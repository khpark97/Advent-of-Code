## STARTER CODE
file = open('2017/Day10_data.txt', 'r')
data = file.read()

# PART 1

import re
lengths = [int(x) for x in re.findall(r'\d+', data)]

input = [e for e in range(256)]

pos, skip = 0, 0
def knot(elements, lengths):
    global pos, skip
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
    return elements

input = knot(input, lengths)

print(f"Part 1: {input[0] * input[1]}")

# PART 2

lengths = [ord(char) for char in data] + [17, 31, 73, 47, 23]

pos, skip = 0, 0
input = [e for e in range(256)]
for _ in range(64):
    input = knot(input, lengths)

dense = []
for i in range(16):
    section = input[i*16:(i+1)*16]
    res = section[0]
    for j in section[1:]:
        res ^= j
    dense.append(res)

result = ''.join([f"{x:02x}" for x in dense])

print(f"Part 2: {result}")