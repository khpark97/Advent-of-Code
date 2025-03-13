## STARTER CODE
file = open('2015/Day03_data.txt', 'r')
data = file.read()

# PART 1

x, y = 0, 0
seen1 = set([(0, 0)])

dirs = {'>': (1, 0), '^': (0, 1), '<': (-1, 0), 'v': (0, -1)}

for d in data:
    dx, dy = dirs[d]
    x += dx
    y += dy
    seen1.add((x, y))

print(f"Part 1: {len(seen1)}")

# PART 2

sx, sy = 0, 0
rx, ry = 0, 0
seen2 = set([(0, 0)])

for i in range(len(data)):
    dx, dy = dirs[data[i]]
    if i % 2 == 0:
        sx += dx
        sy += dy
        seen2.add((sx, sy))

    else:
        rx += dx
        ry += dy
        seen2.add((rx, ry))

print(f"Part 2: {len(seen2)}")