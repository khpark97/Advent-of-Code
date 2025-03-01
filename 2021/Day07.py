## STARTER CODE
file = open('2021/Day07_data.txt', 'r')
data = file.read()

# PART 1

crabs = [int(x) for x in data.split(',')]
median = sorted(crabs)[len(crabs)//2]

score = 0
for c in crabs:
    score += abs(c - median)

print(f"Part 1: {score}")

# PART 2

mean_up = round(sum(crabs)/len(crabs))
mean_down = sum(crabs)//len(crabs)

score_up, score_down = 0, 0
for c in crabs:
    score_up += abs(c - mean_up) * (abs(c - mean_up) + 1) // 2
    score_down += abs(c - mean_down) * (abs(c - mean_down) + 1) // 2
    
print(f"Part 2: {score_up, score_down}")