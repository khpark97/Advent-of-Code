## STARTER CODE
file = open('2015/Day19_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import defaultdict

replacements = defaultdict(list)
i = 0
while lines[i]:
    m, r = lines[i].split(' => ')
    replacements[m].append(r)
    i += 1

distinct = set()
molecule = lines[-1]

for j in range(len(molecule)):
    check = [molecule[j]]
    if j < len(molecule)-1:
        check.append(molecule[j:j+2])
    for c in check:
        if c in replacements:
            for r in replacements[c]:
                distinct.add(''.join([molecule[:j], r, molecule[j+len(c):]]).strip())    

print(f"Part 1: {len(distinct)}")

# PART 2



print(f"Part 2: {len(distinct)}")