## STARTER CODE
file = open('Day14_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
pos, vel = [], []
for line in lines:
    p, v = line.split()
    pos.append([int(k) for k in p[2:].split(',')])
    vel.append([int(k) for k in v[2:].split(',')])
# print(pos, vel)
# print(pos)
# print(vel)
col, row = 103, 101
for i in range(len(pos)):
    p, v = pos[i], vel[i]
    p[0] = (p[0] + 100 * v[0]) % row
    p[1] = (p[1] + 100 * v[1]) % col
    pos[i] = p
# print(pos)

c1 = [range(0, col // 2), range(0, row // 2)]
c2 = [range(col // 2 + 1, col), range(0, row // 2)]
c3 = [range(0, col // 2), range(row // 2 + 1, row)]
c4 = [range(col // 2 + 1, col), range(row // 2 + 1, row)]
q1, q2, q3, q4 = 0, 0, 0, 0
# print(c1, c2, c3, c4)

for j in range(len(pos)):
    curr = pos[j]
    # print(curr)
    if curr[0] in c1[1] and curr[1] in c1[0]:
        q1 += 1
    elif curr[0] in c2[1] and curr[1] in c2[0]:
        q2 += 1
    elif curr[0] in c3[1] and curr[1] in c3[0]:
        q3 += 1
    elif curr[0] in c4[1] and curr[1] in c4[0]:
        q4 += 1

# print(q1, q2, q3, q4)
print(f"Part 1: {q1*q2*q3*q4}")

# PART 2
from matplotlib import pyplot as plt

pos, vel = [], []
for line in lines:
    p, v = line.split()
    pos.append([int(k) for k in p[2:].split(',')])
    vel.append([int(k) for k in v[2:].split(',')])
# print(pos, vel)

col, row = 103, 101
egg = 0

temp = [x.copy() for x in pos]
for k in range(101*103):
    pos = [x.copy() for x in temp]
    for i in range(len(pos)):
        p, v = pos[i], vel[i]
        p[0] = (p[0] + (k * v[0])) % row
        p[1] = (p[1] + (k * v[1])) % col
        pos[i] = p

    c1 = [range(0, col // 2), range(0, row // 2)]
    c2 = [range(col // 2 + 1, col), range(0, row // 2)]
    c3 = [range(0, col // 2), range(row // 2 + 1, row)]
    c4 = [range(col // 2 + 1, col), range(row // 2 + 1, row)]
    q1, q2, q3, q4 = 0, 0, 0, 0
    # print(c1, c2, c3, c4)

    for j in range(len(pos)):
        curr = pos[j]
        # print(curr)
        if curr[0] in c1[1] and curr[1] in c1[0]:
            q1 += 1
        elif curr[0] in c2[1] and curr[1] in c2[0]:
            q2 += 1
        elif curr[0] in c3[1] and curr[1] in c3[0]:
            q3 += 1
        elif curr[0] in c4[1] and curr[1] in c4[0]:
            q4 += 1
    print(k, q1, q2, q3, q4)
    if max(q1, q2, q3, q4) > 170:
        x, y = [p[0] for p in pos], [p[1] for p in pos]
        egg = k
        plt.scatter(x=x, y=y)
        plt.show()
    else:
        egg += 1

#6243
print(f"Part 2: {egg}")