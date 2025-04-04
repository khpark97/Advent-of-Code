## STARTER CODE
file = open('2016/Day18_data.txt', 'r')
start = file.read()

# PART 1

def lengthen(n):
    rows = [start]
    k = 0
    while len(rows) < n:
        curr = ''.join(['.', rows[k], '.'])
        next = []
        for i in range(len(curr) - 2):
            l, c, r = curr[i], curr[i+1], curr[i+2]
            if l == '^':
                if r == '.':
                    next.append('^')
                else:
                    next.append('.')
            elif r == '^':
                next.append('^')
            else:
                next.append('.')
            
        rows.append(''.join(next))
        k += 1
    return rows

import re
tiles_p1 = sum([len(re.findall(r'\.', row)) for row in lengthen(40)])

print(f"Part 1: {tiles_p1}")

# PART 2

tiles_p2 = sum([len(re.findall(r'\.', row)) for row in lengthen(400000)])

print(f"Part 2: {tiles_p2}")