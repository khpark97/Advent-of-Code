## STARTER CODE
file = open('2017/Day10_data.txt', 'r')
data = file.read()

# PART 1

import re

def knot_p1(elements, lengths, pos, skip):
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
    return elements, pos, skip

# PART 2

def knot_p2(key):
    lengths = [ord(char) for char in key] + [17, 31, 73, 47, 23]

    pos, skip = 0, 0
    input = [e for e in range(256)]
    for _ in range(64):
        res = knot_p1(input, lengths, pos, skip)
        input = res[0]
        pos, skip = res[1:]

    dense = []
    for i in range(16):
        section = input[i*16:(i+1)*16]
        res = section[0]
        for j in section[1:]:
            res ^= j
        dense.append(res)

    return ''.join([f"{x:02x}" for x in dense])

if __name__ == "__main__":
    lengths = [int(x) for x in re.findall(r'\d+', data)]

    input = [e for e in range(256)]
    
    input = knot_p1(input, lengths, 0, 0)[0]

    print(f"Part 1: {input[0] * input[1]}")

    print(f"Part 2: {knot_p2(data)}")