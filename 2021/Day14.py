## STARTER CODE
file = open('2021/Day14_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

template = lines[0]
rules = {}
for i in range(2, len(lines)):
    pair, insert = lines[i].split(' -> ')
    rules[pair] = insert

def step(curr):
    i = 0
    while i < len(curr) - 1:
        pair = curr[i] + curr[i+1]
        if pair in rules:
            i += 1
            curr = curr[:i] + rules[pair] + curr[i:]
        i += 1
    return curr

for j in range(10):
    template = step(template)

count = [template.count(c) for c in set(template)]

print(f"Part 1: {max(count) - min(count)}")

# PART 2



count = [template.count(c) for c in set(template)]

print(f"Part 2: {max(count) - min(count)}")