## STARTER CODE
file = open('Day24_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
i = 0
vars = {}
while i < len(lines):
    if lines[i] == '':
        i += 1
        break
    var, val = lines[i].split()
    vars[var[:-1]] = int(val)
    i += 1

z = {}
q = deque([j.split()[:3] + [j.split()[-1]] for j in lines[i:]])
while q:
    i1, o, i2, e = q.popleft()
    if i1 in vars and i2 in vars:
        match o:
            case 'AND': res = vars[i1] and vars[i2]
            case 'XOR': res = vars[i1] ^ vars[i2]
            case 'OR': res = vars[i1] or vars[i2]
        
        if e[0] == 'z':
            z[e] = res
        vars[e] = res
    else:
        q.append([i1, o, i2, e])

binary = ''
for key in sorted(z.keys(), reverse=True):
    binary += str(z[key])

print(f"Part 1: {int(binary, 2)}")

# PART 2
i = 0
vars = {}
x, y = {}, {}
while i < len(lines):
    if lines[i] == '':
        i += 1
        break
    var, val = lines[i].split()
    vars[var[:-1]] = int(val)
    if var[0] == 'x':
        x[var] = val
    elif var[0] == 'y':
        y[var] = val
    i += 1

x_val, y_val = '', ''
for key in sorted(x.keys(), reverse=True):
    x_val += str(x[key])
for key in sorted(y.keys(), reverse=True):
    y_val += str(y[key])

print(x_val, y_val)
add = int(x_val, 2) + int(y_val, 2)
diffs = bin(add ^ int(binary, 2))
print(bin(add)[2:], binary, diffs[2:])
indices = []
for i in range(len(diffs[2:])):
    if diffs[-(i+1)] == '1':
        indices.append('z'+str(i))

# z = {}
# q = deque([j.split()[:3] + [j.split()[-1]] for j in lines[i:]])
# while q:
#     i1, o, i2, e = q.popleft()
#     if i1 in vars and i2 in vars:
#         match o:
#             case 'AND': res = vars[i1] and vars[i2]
#             case 'XOR': res = vars[i1] ^ vars[i2]
#             case 'OR': res = vars[i1] or vars[i2]
        
#         if e[0] == 'z':
#             z[e] = res
#         vars[e] = res
#     else:
#         q.append([i1, o, i2, e])

res = []

print(f"Part 2: {','.join(res)}")