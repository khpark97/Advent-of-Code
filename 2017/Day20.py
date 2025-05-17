## STARTER CODE
file = open('2017/Day20_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import math, re
from collections import defaultdict

particles = defaultdict(dict)
slowest = (float('inf'), 0)
for i in range(len(lines)):
    values = [int(x) for x in re.findall(r'-?\d+', lines[i])]
    particles[i]['p'] = values[0:3]
    particles[i]['v'] = values[3:6]
    particles[i]['a'] = values[6:9]
    accel = math.sqrt(sum([v**2 for v in values[6:9]]))
    if accel < slowest[0]:
        slowest = (accel, i)

print(f"Part 1: {slowest[1]}")

# PART 2

from collections import Counter

def tick():
    for i in particles:
        p, v, a = particles[i].values()
        v = list(map(sum, zip(v, a)))
        particles[i]['v'] = v
        p = list(map(sum, zip(p, v)))
        particles[i]['p'] = p
    
    positions = [tuple(particles[i]['p']) for i in particles]
    remove = []
    for pos, c in Counter(positions).items():
        if c > 1:
            remove.append(list(pos))

    indices = []
    for j in particles:
        if particles[j]['p'] in remove:
            indices.append(j)

    for removal in indices:
        particles.pop(removal)

for _ in range(100):
    tick()

print(f"Part 2: {len(particles)}")