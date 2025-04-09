## STARTER CODE
file = open('2016/Day22_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
all_nodes = []
for l in lines[2:]:
    x, y, size, used, avail, percentage = [int(x) for x in re.findall(r'\d+', l)]
    all_nodes.append((x, y, size, used, avail))

viable = 0
for i in range(len(all_nodes)):
    used = all_nodes[i][3]
    if used != 0:
        for j in range(len(all_nodes)):
            if i != j:
                avail = all_nodes[j][4]
                if avail >= used:
                    viable += 1

print(f"Part 1: {viable}")

# PART 2

print(f"Part 2: {viable}")