## STARTER CODE
file = open('2015/Day13_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import defaultdict
from itertools import permutations

network = defaultdict(int)
people = set()

for l in lines:
    words = l.strip('.').split()
    p1, _, change, val, *_, p2 = words
    people.add(p1)
    people.add(p2)
    network[tuple(sorted((p1, p2)))] += int(val) if change == 'gain' else -int(val)

def sit(n, p):
    happiness = 0
    for p in permutations(p):
        curr = n[tuple(sorted((p[0], p[-1])))]
        for i in range(len(p) - 1):
            curr += n[tuple(sorted((p[i], p[i+1])))]
        happiness = max(happiness, curr)

    return happiness

print(f"Part 1: {sit(network, people)}")

# PART 2

for p in people:
    network[tuple(sorted((p, 'me')))] = 0
people.add('me')

print(f"Part 2: {sit(network, people)}")