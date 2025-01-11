## STARTER CODE
file = open('Day7_data', 'r')
data = file.read()
lines = data.splitlines()

from itertools import product

# PART 1
equations = []
for line in lines:
    split = line.split()
    target, values = int(split[0][:-1]), list(map(int, split[1:]))
    equations.append((target, values))

def combination(target, values):
    for combo in product("*+", repeat=len(values) - 1):
        ans = values[0]
        for i in range(1, len(values)):
            if combo[i-1] == '+':
                ans += values[i]
            else:
                ans *= values[i]
        if ans == target:
            return target
    return 0

total = 0
for t, v in equations:
    total += combination(t, v)
print(total)

# PART 2

def combination(target, values):
    for combo in product("*+|", repeat=len(values) - 1):
        ans = values[0]
        for i in range(1, len(values)):
            if combo[i-1] == '+':
                ans += values[i]
            elif combo[i-1] == '*':
                ans *= values[i]
            else:
                ans = int(str(ans) + str(values[i]))
        if ans == target:
            return target
    return 0

total = 0
for t, v in equations:
    total += combination(t, v)
print(total)