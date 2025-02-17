## STARTER CODE
file = open('2022/Day14_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

rocks = []
for line in lines:
    rocks.append(line.split(' -> '))

walls = set()
range_x, range_y = [float('inf'), -float('inf')], [0, -float('inf')]

for path in rocks:
    cx, cy = map(int, path[0].split(','))
    range_x = [min(range_x[0], cx), max(range_x[1], cx)]
    range_y = [min(range_y[0], cy), max(range_y[1], cy)]
    for i in range(len(path) - 1):
        cx, cy = map(int, path[i].split(','))
        nx, ny = map(int, path[i + 1].split(','))
        range_x = [min(range_x[0], nx), max(range_x[1], nx)]
        range_y = [min(range_y[0], ny), max(range_y[1], ny)]
        if nx - cx == 0:
            for j in range(abs(ny - cy) + 1):
                walls.add((cx, max(ny, cy) - j))
        else:
            for j in range(abs(nx - cx) + 1):
                walls.add((max(nx, cx) - j, cy))
range_x[1] += 1
range_y[1] += 1

score = 0
trial = walls.copy()
def sand(x, y):
    for nx, ny in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if nx not in range(*range_x) or ny not in range(*range_y):
            return -1
        if (nx, ny) not in trial:
            return sand(nx, ny)
    trial.add((x, y))
    return 1

while True:
    s = sand(500, 0)
    if s == -1:
        break
    else:
        score += 1
        
print(f"Part 1: {score}")

# PART 2

trial = walls.copy()
floor = range_y[1]+1
for k in range(-floor, floor+1):
    trial.add((500+k, floor))

score = 0
def sand(x, y):
    for nx, ny in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if (nx, ny) not in trial:
            return sand(nx, ny)
    trial.add((x, y))
    if (500, 0) in trial:
        return -1
    return 1

while True:
    s = sand(500, 0)
    if s == -1:
        score += 1
        break
    else:
        score += 1

print(f"Part 2: {score}")