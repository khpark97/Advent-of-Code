## STARTER CODE
file = open('2016/Day15_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

def turn(discs):
    for d in discs:
        range, curr = discs[d]
        discs[d] = (range, (curr+1) % range)

def check(discs):
    for d in discs:
        range, curr = discs[d]
        if curr != range - d:
            return False
    return True

import re
discs_p1 = {}
for l in lines:
    disc, range, _, start = [int(x) for x in re.findall(r"\d+", l)]
    discs_p1[disc] = (range, start)

discs_p2 = discs_p1.copy()
discs_p2[len(discs_p2) + 1] = (11, 0)

t = 0
while True:
    if check(discs_p1):
        break
    t += 1
    turn(discs_p1)

print(f"Part 1: {t}")

# PART 2

t = 0
while True:
    if check(discs_p2):
        break
    t += 1
    turn(discs_p2)

print(f"Part 2: {t}")