## STARTER CODE
file = open('2015/Day12_data.txt', 'r')
data = file.read()

# PART 1

import re

total = sum([int(x) for x in re.findall(r'-?\d+', data)])

print(f"Part 1: {total}")

# PART 2

import json

parsed = json.loads(data)

def find(object):
    if 'red' in json.dumps(object):
        for sub in object:
            print(sub)
            find(sub)
    
find(parsed[0])

# for obj in parsed[5:]:
#     if 'red' in obj:
#         print(obj)
#         break
#     print(len(obj), 'red' in json.dumps(obj), 'red' in obj)

x = json.dumps(parsed[0][1][0], indent=4)

print(f"Part 2: {total}")