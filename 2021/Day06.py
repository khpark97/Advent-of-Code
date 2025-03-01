## STARTER CODE
file = open('2021/Day06_data.txt', 'r')
data = file.read()

# PART 1

fish = [int(x) for x in data.split(',')]
lanternfish = {i:0 for i in range(9)}
for f in set(fish):
    lanternfish[f] = fish.count(f)

for day in range(80):
    temp = lanternfish[0]
    for i in range(len(lanternfish)-1):
        lanternfish[i] = lanternfish[i+1]
    lanternfish[6] += temp
    lanternfish[8] = temp

score = sum(lanternfish.values())

print(f"Part 1: {score}")

# PART 2

for day in range(256-80):
    temp = lanternfish[0]
    for i in range(len(lanternfish)-1):
        lanternfish[i] = lanternfish[i+1]
    lanternfish[6] += temp
    lanternfish[8] = temp

score = sum(lanternfish.values())

print(f"Part 2: {score}")