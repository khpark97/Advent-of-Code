## STARTER CODE
file = open('Day20_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
start, end = (), ()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'S':
            start = (r, c)
        elif lines[r][c] == 'E':
            end = (r, c)
            lines[r] = lines[r][:c] + '.' + lines[r][c+1:]
# print(start, end)

def run():
    score = 0
    path = {start: 0}
    curr = start
    while curr != end:
        # print(curr)
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = tuple(map(sum, zip(curr, dir)))
            if (nr, nc) not in path and lines[nr][nc] == '.':
                curr = (nr, nc)
                score += 1
                path[curr] = score
                # print(path)
                break
    return path

path = run()
total = 0
def cheat(curr):
    shortcuts = 0
    for dir in [(0, 2), (0, -2), (2, 0), (-2, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]:
        nr, nc = tuple(map(sum, zip(curr, dir)))
        if nr in range(len(lines)) and nc in range(len(lines[0])) and lines[nr][nc] == '.':
            if path[(nr, nc)] - (path[curr] + 2) >= 100:
                shortcuts += 1
    return shortcuts

for coord in path:
    total += cheat(coord)

print(f"Part 1: {total}")

# PART 2
twenty = [(r, c) for r in range(-20, 21) for c in range(-20, 21) if abs(r)+abs(c)<=20]
def cheat_two(curr):
    shortcuts = 0
    for dir in twenty:
        save = sum([abs(i) for i in dir])
        nr, nc = tuple(map(sum, zip(curr, dir)))
        if nr in range(len(lines)) and nc in range(len(lines[0])) and lines[nr][nc] == '.':
            if path[(nr, nc)] - (path[curr] + save) >= 100:
                shortcuts += 1
    return shortcuts

total = 0
for coord in path:
    total += cheat_two(coord)

print(f"Part 2: {total}")