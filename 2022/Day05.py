## STARTER CODE
file = open('2022/Day05_data.txt', 'r')
data = file.read()
lines = data.splitlines()

cols = 9
# PART 1

i = 0
crates = [[].copy() for i in range(cols)]
moves = []
while i < len(lines):
    line = lines[i].split()
    if str.isdigit(line[0]):
        i += 1
    elif line[0] == 'move':
        moves.append([int(line[1]), int(line[3]), int(line[5])])
    elif line[0][0] == '[':
        for j in range((len(lines[i])+1)//4):
            crate = lines[i][1+j*4]
            if str.isalpha(crate):
                crates[j].append(crate)
    i += 1

def move(s, e):
    crates[e] = [crates[s][0]] + crates[e]
    crates[s] = crates[s][1:]

for m in moves:
    for k in range(m[0]):
        move(m[1]-1, m[2]-1)

res = ''
for col in crates:
    res += col[0]

print(f"Part 1: {res}")

# PART 2

i = 0
crates = [[].copy() for i in range(cols)]
moves = []
while i < len(lines):
    line = lines[i].split()
    if str.isdigit(line[0]):
        i += 1
    elif line[0] == 'move':
        moves.append([int(line[1]), int(line[3]), int(line[5])])
    elif line[0][0] == '[':
        for j in range((len(lines[i])+1)//4):
            crate = lines[i][1+j*4]
            if str.isalpha(crate):
                crates[j].append(crate)
    i += 1

def move(c, s, e):
    crates[e] = crates[s][:c] + crates[e]
    crates[s] = crates[s][c:]

for m in moves:
    move(m[0], m[1]-1, m[2]-1)
    
res = ''
for col in crates:
    res += col[0]

print(f"Part 2: {res}")