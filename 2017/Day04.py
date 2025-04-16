## STARTER CODE
file = open('2017/Day04_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import Counter

valid_p1, valid_p2 = 0, 0
for l in lines:
    split = l.split()
    most = Counter(split).most_common(1).pop()
    if most[1] == 1:
        valid_p1 += 1

    anagram = False
    for i in range(len(split)):
        count = Counter(split[i])
        for j in range(i+1, len(split)):
            if Counter(split[j]) == count:
                anagram = True
    valid_p2 += 0 if anagram else 1

print(f"Part 1: {valid_p1}")

# PART 2

print(f"Part 2: {valid_p2}")