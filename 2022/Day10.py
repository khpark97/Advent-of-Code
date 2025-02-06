## STARTER CODE
file = open('2022/Day10_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

score = 0
x = 1
cycle = 1
for l in lines:
    p = l.split()
    if p[0] == 'addx':
        cycle += 1
        if (cycle + 20) % 40 == 0:
            score += cycle * x
        x += int(p[1])
    cycle += 1
    if (cycle + 20) % 40 == 0:
        score += cycle * x

print(f"Part 1: {score}")

# PART 2

res = []
curr = ''
x = 1
cycle = 0
for l in lines:
    if len(curr) in range(x-1, x+2):
        curr += '#'
    else:
        curr += '.'
    cycle += 1
    if cycle % 40 == 0:
        res.append(curr)
        curr = ''
    p = l.split()
    if p[0] == 'addx':
        if len(curr) in range(x-1, x+2):
            curr += '#'
        else:
            curr += '.'
        cycle += 1
        if cycle % 40 == 0:
            res.append(curr)
            curr = ''
        x += int(p[1])

print("Part 2: ")
for r in res:
    print(r)