## STARTER CODE
file = open('2015/Day24_data.txt', 'r')
data = file.read()

# PART 1

from itertools import combinations
import math

presents = [int(p) for p in data.splitlines()]

def entanglement(n):
    weight = sum(presents) // n
    quantum, smallest = float('inf'), float('inf')
    for i in range(len(presents)): 
            #range(len(presents) // n + 2) works much faster but i dont know why
        for c in combinations(presents, i):
            if len(c) <= smallest and sum(c) == weight:
                smallest = len(c)
                quantum = min(math.prod(c), quantum)
    return quantum

print(f"Part 1: {entanglement(3)}")

# PART 2

print(f"Part 2: {entanglement(4)}")