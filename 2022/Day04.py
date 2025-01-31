## STARTER CODE
file = open('2022/Day04_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
total = 0
for line in lines:
    l, r = [([int(x) for x in pair.split('-')]) for pair in line.split(',')]
    
    if (l[0] >= r[0] and l[1] <= r[1]) or (l[0] <= r[0] and l[1] >= r[1]):
        total += 1

print(f"Part 1: {total}")

# PART 2
total = 0
for line in lines:
    l, r = [([int(x) for x in pair.split('-')]) for pair in line.split(',')]

    if l[0] in range(r[0], r[1]+1) or l[1] in range(r[0], r[1]+1) or r[0] in range(l[0], l[1]+1) or r[1] in range(l[0], l[1]+1):
        total += 1

print(f"Part 2: {total}")