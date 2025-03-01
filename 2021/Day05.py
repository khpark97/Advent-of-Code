## STARTER CODE
file = open('2021/Day05_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

field = [[0] * 1000 for _ in range(1000)]

for line in lines:
    start, end = [[int(i) for i in x.split(',')] for x in line.split(' -> ')]
    if start[0] != end[0] and start[1] != end[1]:
        continue
    if start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            field[start[1]][i] += 1
    else:
        for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            field[j][start[0]] += 1

score = 0
for r in range(len(field)):
    for c in range(len(field[0])):
        if field[r][c] >= 2:
            score += 1

print(f"Part 1: {score}")

# PART 2

for line in lines:
    start, end = [[int(i) for i in x.split(',')] for x in line.split(' -> ')]
    if start[0] != end[0] and start[1] != end[1]:
        if end[0] > start[0] and end[1] > start[1]: #0,0 - 8,8
            for i in range(end[0] + 1 - start[0]):
                field[start[1] + i][start[0] + i] += 1
        elif end[0] < start[0] and end[1] > start[1]: #8,0 - 0,8
            for i in range(end[1] + 1 - start[1]):
                field[start[1] + i][start[0] - i] += 1
        elif end[0] < start[0] and end[1] < start[1]: #6,4 - 2,0
            for i in range(start[1] + 1 - end[1]):
                field[start[1] - i][start[0] - i] += 1
        else: #5,5 - 8,2
            for i in range(end[0] + 1 - start[0]):
                field[start[1] - i][start[0] + i] += 1        

score = 0
for r in range(len(field)):
    for c in range(len(field[0])):
        if field[r][c] >= 2:
            score += 1
            
print(f"Part 2: {score}")