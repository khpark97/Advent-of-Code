## STARTER CODE
file = open('2022/Day15_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
import re

sensors, beacons = [], []
for l in lines:
    s, b = [re.findall(r'-?\d+', part) for part in l.split(':')]
    sensors.append(tuple(int(i) for i in s))
    beacons.append(tuple(int(i) for i in b))

def mh(a, b):
    return sum([abs(int(i) - int(j)) for i, j in zip(a, b)])

target = 2000000
positions = set()
# for i in range(len(sensors)):
#     s, b = sensors[i], beacons[i]
#     diff = mh(s, b) - abs(target - s[1])
#     if diff >= 0:
#         for j in range(s[0] - diff, s[0] + diff + 1):
#             pos = (j, target)
#             if pos not in beacons and pos not in sensors:
#                 positions.add((j, target))

print(f"Part 1: {len(positions)}")

# PART 2

sensors, beacons = zip(*sorted(zip(sensors, beacons)))
print(sensors, beacons)

print(f"Part 2: {len(positions)}")