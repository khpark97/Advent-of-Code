## STARTER CODE
file = open('Day5_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict

# PART 1
pairs = [line.split("|") for line in lines[:1176]]
orders = [line.split(",") for line in lines[1177:]]

prereqs = defaultdict(list)
for s, e in [pair for pair in pairs]:
    prereqs[e].append(s)

def check(order):
    i = 0
    while i < len(order) - 1:
        curr = order[i]
        for j in order[i+1:]:
            if j in prereqs[curr]:
                return False
        i += 1
    return order[len(order)//2]

total = 0
for order in orders:
    x = check(order)
    if x:
        total += int(x)
print(total)

# PART 2
def update(order):
    i = 0
    incorrect = False
    while i < len(order) - 1:
        ptr = i
        curr = order[ptr]
        for j in range(len(order) - 1, i, -1):
            if order[j] in prereqs[curr]:
                incorrect = True
                order[ptr] = order[j]
                order[j] = curr
                ptr = j
                i -= 1
                break
        i += 1
    return order[len(order)//2] if incorrect else 0

total = 0
for order in orders:
    x = update(order)
    total += int(x)
print(total)
