## STARTER CODE
file = open('2016/Day01_data.txt', 'r')
data = file.read()

# PART 1

instructions = data.split(", ")
seen = set([(0, 0)])
x, y = 0, 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i = 0
repeat = float('inf')
for move in instructions:
    turn, dist = move[0], int(move[1:])
    if turn == 'R': i += 1
    else: i -= 1
    i %= 4
    dx, dy = directions[i]
    for j in range(dist):
        x += dx
        y += dy
        if (x, y) in seen and repeat == float('inf'):
            repeat = (x, y)
        seen.add((x, y))

print(f"Part 1: {abs(x) + abs(y)}")

# PART 2

print(f"Part 2: {sum([abs(i) for i in repeat])}")