## STARTER CODE
file = open('2017/Day15_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
generators = {}
generators['A'] = int(re.findall(r'\d+', lines[0])[0])
generators['B'] = int(re.findall(r'\d+', lines[1])[0])

score = 0
for _ in range(40000000):
    generators['A'] = (generators['A'] * 16807) % 2147483647
    generators['B'] = (generators['B'] * 48271) % 2147483647
    if f"{generators['A']:032b}"[-16:] == f"{generators['B']:032b}"[-16:]:
        score += 1

print(f"Part 1: {score}")

# PART 2

score = 0
for _ in range(5000000):
    generators['A'] = (generators['A'] * 16807) % 2147483647
    generators['B'] = (generators['B'] * 48271) % 2147483647
    while generators['A'] % 4 != 0:
        generators['A'] = (generators['A'] * 16807) % 2147483647
    while generators['B'] % 8 != 0:
        generators['B'] = (generators['B'] * 48271) % 2147483647
    if f"{generators['A']:032b}"[-16:] == f"{generators['B']:032b}"[-16:]:
        score += 1

print(f"Part 2: {score}")