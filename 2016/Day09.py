## STARTER CODE
file = open('2016/Day09_data.txt', 'r')
data = file.read()

# PART 1

import re

i, length = 0, 0
while i < len(data):
    curr = data[i]
    if curr == '(':
        digits = re.findall(r'\d+', data[i:])
        if digits:
            a, b = [int(x) for x in digits[:2]]
            i += data[i:].index(')') + a
            length += a * b
    else:
        length += 1
    i += 1

print(f"Part 1: {length}")

# PART 2

def decompress(i, a, b):
    curr = data[i:i+a]
    x = re.findall(r'\(|\)', curr)
    if x:
        print(x)
    else:
        return a

i, length = 0, 0
# while i < len(data):
#     curr = data[i]
#     if curr == '(':
#         digits = re.findall(r'\d+', data[i:])
#         if digits:
#             a, b = [int(x) for x in digits[:2]]
#             length += decompress(i, a, b)
#     else:
#         length += 1
#     i += 1

# print(decompress(1, 8, 2))

print(f"Part 2: {length}")