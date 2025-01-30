## STARTER CODE
file = open('Day4_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict

# PART 1
rows = len(lines)
cols = len(lines[0])

def search(x, y, dx, dy):
    chars = ['X']
    while len(chars) < 4:
        x = x + dx
        y = y + dy
        if x >= rows or x < 0 or y >= cols or y < 0:
            return False
        chars.append(lines[x][y])
    return chars == ['X', 'M', 'A', 'S']

total = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X':
            for dx, dy in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
                if search(i, j, dx, dy):
                    total += 1
print(total)

# PART 2
rows = len(lines)
cols = len(lines[0])

def search(x, y):
    chars = []
    for dx, dy in [[-1, -1], [1, 1], [-1, 1], [1, -1]]:
        new_x = x + dx
        new_y = y + dy
        if new_x >= rows or new_x < 0 or new_y >= cols or new_y < 0:
            return False
        chars.append(lines[new_x][new_y])
    if chars[:2] == ['S', 'M'] or chars[:2] == ['M', 'S']:
        return chars[2:] == ['S', 'M'] or chars[2:] == ['M', 'S']

total = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'A':
            if search(i, j):
                total += 1
print(total)
