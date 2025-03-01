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
    if start[0] != end[0] and start[1] != end[1]:  # Diagonal lines only
        dx = 1 if end[0] > start[0] else -1  # Step direction for x
        dy = 1 if end[1] > start[1] else -1  # Step direction for y
        length = abs(end[0] - start[0])  # Number of steps
        
        for i in range(length + 1):  # Include the last point
            field[start[1] + i * dy][start[0] + i * dx] += 1      

score = 0
for r in range(len(field)):
    for c in range(len(field[0])):
        if field[r][c] >= 2:
            score += 1
            
print(f"Part 2: {score}")