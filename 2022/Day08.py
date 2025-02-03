## STARTER CODE
file = open('2022/Day08_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

total = 0

def scan(r, c, d):
    tree = lines[r][c]
    r, c = tuple(map(sum, zip((r, c), d)))
    while r in range(len(lines)) and c in range(len(lines[0])):
        next = lines[r][c]
        if next >= tree:
            return False
        r, c = tuple(map(sum, zip((r, c), d)))
    return True

for r in range(len(lines)):
    for c in range(len(lines[0])):
        visible = False
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if scan(r, c, d):
                visible = True
                break
        if visible:
            total += 1

print(f"Part 1: {total}")

# PART 2

def scan(r, c, d):
    scenic = 0
    tree = lines[r][c]
    r, c = tuple(map(sum, zip((r, c), d)))
    while r in range(len(lines)) and c in range(len(lines[0])):
        next = lines[r][c]
        if next >= tree:
            return scenic + 1
        scenic += 1
        r, c = tuple(map(sum, zip((r, c), d)))
    return scenic

high = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        views = 1
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            views *= scan(r, c, d)
        high = max(high, views)

print(f"Part 2: {high}")