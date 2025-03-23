## STARTER CODE
file = open('2015/Day20_data.txt', 'r')
data = file.read()

# PART 1

import math

presents = int(data)

n = presents
houses = [0 for _ in range(n//10 + 1)]
for i in range(1, n//10 + 1):
    for j in range(i, n//10 + 1, i):
        houses[j] += i * 10

for j in range(len(houses)):
    if houses[j] > presents:
        house = j
        break

print(f"Part 1: {house}")

# PART 2

houses = [0 for _ in range(n//10 + 1)]
for i in range(1, n//10 + 1):
    for j in range(i, min(n//10 + 1, i * 50 + 1) , i):
        houses[j] += i * 10

for j in range(len(houses)):
    if houses[j] > presents:
        house = j
        break
    

print(f"Part 2: {house}")