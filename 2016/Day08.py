## STARTER CODE
file = open('2016/Day08_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re

rows, cols = 6, 50
screen = [[0 for _ in range(cols)] for _ in range(rows)]
for l in lines:
    a, b = [int(x) for x in re.findall(r"\d+", l)]
    command, op = l.split()[:2]
    if command == "rect":
        for r in range(b):
            for c in range(a):
                screen[r][c] = 1
    else:
        if op == "row":
            screen[a] = screen[a][-b:] + screen[a][:-b]
        elif op == "column":
            col = [screen[r][a] for r in range(rows)]
            rotated = col[-b:] + col[:-b]
            for i in range(rows):
                screen[i][a] = rotated[i]
    # print(screen)
        
lit = sum([sum(row) for row in screen])
print(f"Part 1: {lit}")

# PART 2

print("Part 2:")
for row in screen:
    print(''.join(['#' if x == 1 else '.' for x in row]))