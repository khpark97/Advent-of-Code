## STARTER CODE
file = open('Day25_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
locks, keys = [], []
for i in range(0, len(lines), 8):
    cols = [0] * 5
    for j in range(1, 6):
        cols = [cols[k] + 1 if lines[i+j][k] == '#' else cols[k] for k in range(5)]
    if lines[i] == '#####':
        locks.append(cols)
    else:
        keys.append(cols)

total = 0
for k in keys:
    for l in locks:
        if max([k[i] + l[i] for i in range(5)]) <= 5:
            total += 1
            
print(f"Part 1: {total}")

# PART 2
