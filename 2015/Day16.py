## STARTER CODE
file = open('2015/Day16_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re

sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

p1, p2 = -1, -1
for i in range(len(lines)):
    l = lines[i]
    items = [item[:-1] for item in [l.split()[k] for k in [2,4,6]]]
    aunt, *count = [int(x) for x in re.findall(r'\d+', l)]
    
    match_p1, match_p2 = 0, 0

    for c in range(len(items)):
        item = items[c]
        if item in ['cats', 'trees']:
            if sue[item] < count[c]:
                match_p2 += 1
            if sue[item] == count[c]:
                match_p1 += 1
        elif item in ['pomeranians', 'goldfish']:
            if sue[item] > count[c]:
                match_p2 += 1
            if sue[item] == count[c]:
                match_p1 += 1
        else:
            if sue[item] == count[c]:
                match_p1 += 1
                match_p2 += 1

    if match_p1 == 3:
        p1 = aunt
    if match_p2 == 3:
        p2 = aunt

print(f"Part 1: {p1}")

# PART 2

print(f"Part 2: {p2}")