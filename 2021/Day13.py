## STARTER CODE
file = open('2021/Day13_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

dots = set()
folds = []
i = 0
while i < len(lines):
    if not lines[i]:
        i += 1
        while i < len(lines):
            folds.append(lines[i][11:].split('='))
            i += 1
        break
    dots.add(tuple([int(x) for x in lines[i].split(',')]))
    i += 1

part_1 = set()
for j in range(len(folds)):
    if j == 1:
        part_1 = dots
    temp = set()
    axis, val = folds[j][0], int(folds[j][1])
    if axis == 'y':
        for x, y in dots:
            if y > val:
                temp.add((x, -y + 2*val))
            else:
                temp.add((x, y))
    else:
        for x, y in dots:
            if x > val:
                temp.add((-x + 2*val, y))
            else:
                temp.add((x, y))
    dots = temp

print(f"Part 1: {len(part_1)}")

# PART 2

result = []
for i in range(max(dots, key=lambda x: x[1])[1] + 1):
    curr = ''
    for j in range(max(dots, key=lambda x: x[0])[0] + 1):
        if (j, i) in dots:
            curr += '#'
        else:
            curr += '.'
    result.append(curr)

print("Part 2: ")
for r in result:
    print(r)