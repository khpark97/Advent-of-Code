## STARTER CODE
file = open('2015/Day14_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
time_limit = 2503

reindeers = {}
for l in lines:
    r = l.split()[0]
    reindeers[r] = [int(x) for x in re.findall(r'\d+', l)]

furthest = 0
for r in reindeers:
    speed, duration, rest = reindeers[r]
    dist = speed * duration
    time = duration + rest
    while time < time_limit:
        dt = min(time_limit - time, duration)
        dist += speed * dt
        time += dt + rest
    furthest = max(dist, furthest)

print(f"Part 1: {furthest}")

# PART 2

race = {r: 0 for r in reindeers}
points = {r: 0 for r in reindeers}
for i in range(time_limit):
    for r in reindeers:
        speed, duration, rest = reindeers[r]
        cycle = duration + rest
        if i % cycle < duration:
            race[r] += speed
    points[max(race, key=lambda x: race[x])] += 1

print(f"Part 2: {max(points.values())}")