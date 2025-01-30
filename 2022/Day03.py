## STARTER CODE
file = open('2022/Day03_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

score = 0

for rucksack in lines:
    half = len(rucksack)//2
    left, right = set(), set()
    for c in rucksack[:half]:
        left.add(c)
    for c in rucksack[half:]:
        right.add(c)
    shared = left.intersection(right).pop()
    if str.isupper(shared):
        score += ord(shared) - 38
    else:
        score += ord(shared) - 96
        
print(f"Part 1: {score}")

# PART 2

score = 0
i = 0
while i < len(lines):
    first = set(lines[i])
    second = set(lines[i+1])
    third = set(lines[i+2])

    shared = first.intersection(second).intersection(third).pop()
    if str.isupper(shared):
        score += ord(shared) - 38
    else:
        score += ord(shared) - 96
    i += 3

print(f"Part 2: {score}")