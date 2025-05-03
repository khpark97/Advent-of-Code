## STARTER CODE
file = open('2017/Day19_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

start = (0, lines[0].index('|'))
letters = []
dir = 2
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
paths = ['|', '-']
steps = 1
while True:
    start = tuple(map(sum, zip(start, dirs[dir])))
    cr, cc = start
    curr = lines[cr][cc]
    if curr == ' ':
        break
    steps += 1
    if curr.isalpha():
        letters.append(curr)
    elif curr == '+':
        done = 0
        for i in [1, 2]:
            dir = (dir + i) % 4
            nr, nc = tuple(map(sum, zip(start, dirs[dir])))
            next = lines[nr][nc]
            if next != ' ':
                break
            done += 1
        if done == 2:
            break

print(f"Part 1: {''.join(letters)}")

# PART 2

print(f"Part 2: {steps}")