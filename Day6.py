## STARTER CODE
file = open('Day6_data', 'r')
data = file.read()
lines = data.splitlines()

def find():
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == '^':
                return [r, c]
r, c = find()

# PART 1
seen_part1 = set([(r, c)])
pos = [r, c]
def move(r, c, d):
    global pos
    match d: #90 degree turns
        case 0: #up
            next = [r-1, c]
        case 1: #right
            next = [r, c+1]
        case 2: #down
            next = [r+1, c]
        case 3: #left
            next = [r, c-1]
    if next[0] not in range(len(lines)) or next[1] not in range(len(lines[0])):
        return -1
    r, c = next
    if lines[r][c] == '#':
        return (d + 1) % 4
    else:
        seen_part1.add((r, c))
        pos = [r, c]
        return 10
    
ret = 0
dir = 0
while ret != -1:
    ret = move(pos[0], pos[1], dir)
    if ret in range(0, 4):
        dir = ret

print(len(seen_part1))

# PART 2
def run():
    def move(row, col, d):
        nonlocal pos
        match d: #90 degree turns
            case 0: #up
                next = [row-1, col]
            case 1: #right
                next = [row, col+1]
            case 2: #down
                next = [row+1, col]
            case 3: #left
                next = [row, col-1]
        if next[0] not in range(len(lines)) or next[1] not in range(len(lines[0])):
            return -1
        if lines[next[0]][next[1]] == '#': # turn
            return (d + 1) % 4
        else:
            seen.add(((row, col), d))
            pos = [next[0], next[1]]
            return 10
    seen = set()
    pos = [r, c]
    ret = 0
    dir = 0
    while ret != -1:
        ret = move(pos[0], pos[1], dir)
        if ret in range(0, 4):
            dir = ret
        if ((pos[0], pos[1]), dir) in seen:
            return 1
    return 0    

total = 0
for nr, nc in seen_part1:
    temp = lines[nr]
    lines[nr] = lines[nr][:nc] + '#' + lines[nr][nc+1:]
    total += run()
    lines[nr] = temp
print(total)

# traveled = {}
# pos = [r, c]
# total = 0

# def move(r, c, d):
#     global traveled
#     global pos
#     global total
#     match d: #90 degree turns
#         case 0: #up
#             next = [r-1, c]
#         case 1: #right
#             next = [r, c+1]
#         case 2: #down
#             next = [r+1, c]
#         case 3: #left
#             next = [r, c-1]
#     if next[0] not in range(len(lines)) or next[1] not in range(len(lines[0])):
#         return -1
#     if lines[next[0]][next[1]] == '#': # turn
#         return (d + 1) % 4
#     else: # straight
#         if d % 2 == 0:
#             if c in traveled:
#                 dir, row = traveled[c]
#                 if dir == d:
#                     if d == 0:
#                         if row > r:
#                             total += 1
#                     elif d == 2:
#                         if row < r:
#                             total += 1
#         elif d % 2 == 1:
#             if r in traveled:
#                 dir, col = traveled[r]
#                 print(dir, col)
#                 if dir == d:
#                     if d == 1:
#                         if col > c:
#                             total += 1
#                     elif d == 3:
#                         if col < c:
#                             total += 1
#         pos = [next[0], next[1]]
#         return 10

# traveled[c] = (0, r)

# ret = 0
# dir = 0
# while ret != -1:
#     ret = move(pos[0], pos[1], dir)
#     if ret in range(0, 4):
#         dir = ret
#         ret = move(pos[0], pos[1], dir)
#         match dir:
#             case 0: #up
#                 traveled[pos[1]] = (0, pos[0])
#             case 1: #right
#                 traveled[pos[0]] = (1, pos[1])
#             case 2: #down
#                 traveled[pos[1]] = (2, pos[0])
#             case 3: #left
#                 traveled[pos[0]] = (3, pos[1])

# print(total)

# - find starting coordinates of straight runs
# - every forward move, check straight to its right turn and see if its been 
# traveled before in the same direction 
# - if a starting coordinate is in the list, total += 1