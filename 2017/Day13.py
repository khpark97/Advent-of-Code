## STARTER CODE
file = open('2017/Day13_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

layers = {}
end = -1
import re
for line in lines:
    depth, length = [int(x) for x in re.findall(r'\d+', line)]
    layers[depth] = [1, length, 1]
    end = max(end, depth)

def scan(scanners):
    for depth in scanners:
        scanner, length, dir = scanners[depth]
        next = scanner + dir
        scanners[depth][0] = next
        if next == length:
            scanners[depth][2] = -1
        elif next == 1:
            scanners[depth][2] = 1
    return scanners

import copy
def run():
    firewall = copy.deepcopy(layers)
    severity = 0
    pos = -1

    while pos < end:
        pos += 1
        if pos in firewall:
            scanner, length, _ = firewall[pos]
            if scanner == 1:
                severity += pos * length
        firewall = scan(firewall)
    return severity

print(f"Part 1: {run()}")

# PART 2

def delayed(delay):
    for scanner in layers:
        _, length, _ = layers[scanner]
        if (delay + scanner) % ((length - 1) * 2) + 1 == 1:
            return -1
    return 1

delay = 0
result = -1
while result == -1:
    delay += 1
    result = delayed(delay)

print(f"Part 2: {delay}")