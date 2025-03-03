## STARTER CODE
file = open('2021/Day08_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

score = 0
for l in lines:
    output = l.split('|')[1].split()
    for n in output:
        score += 1 if len(n) in [2, 3, 4, 7] else 0

print(f"Part 1: {score}")

# PART 2



print(f"Part 2: {score}")