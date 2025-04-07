## STARTER CODE
file = open('2016/Day21_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
password = list('abcdefgh')
def scramble(pw):
    for k in range(len(lines)):
        operation = lines[k]
        split = operation.split()
        args = [int(i) for i in re.findall(r'\d+', operation)]
        match split[0]:
            case 'swap':
                if 'position' in operation:
                    x, y = args
                    temp = pw[x]
                    pw[x] = pw[y]
                    pw[y] = temp

                elif 'letter' in operation:
                    x, y = split[2], split[5]
                    i, j = pw.index(x), pw.index(y)
                    pw[i] = y
                    pw[j] = x

            case 'rotate':
                if 'step' in operation:
                    x = args[0] % len(pw)
                    if 'left' in split:
                        pw = pw[x:] + pw[:x]

                    elif 'right' in split:
                        pw = pw[-x:] + pw[:-x]

                elif 'position' in operation:
                    x = split[-1]
                    i = pw.index(x)
                    if i >= 4:
                        i += 2
                    else:
                        i += 1
                    i %= len(pw)
                    pw = pw[-i:] + pw[:-i]

            case 'reverse':
                x, y = args
                pw = ''.join(pw)
                pw = list(''.join([pw[:x], pw[x:y+1][::-1], pw[y+1:]]))
                
            case 'move':
                x, y = args
                temp = pw[x]
                pw.remove(pw[x])
                pw.insert(y, temp)
    return ''.join(pw)

print(f"Part 1: {scramble(password)}")

# PART 2

from itertools import permutations
for p in permutations(password):
    p = list(p)
    if scramble(p) == 'fbgdceah':
        start = ''.join(p)
        break

print(f"Part 2: {start}")