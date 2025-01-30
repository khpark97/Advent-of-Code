## STARTER CODE
file = open('Day11_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict

# PART 1
stones = list(map(int, lines[0].split()))

def blink():
    global stones
    i = 0
    while i < len(stones):
        size = len(str(stones[i]))
        if stones[i] == 0:
            stones[i] = 1
        elif size % 2 == 0:
            left = str(stones[i])[:size // 2]
            right = str(stones[i])[size // 2:]
            stones = stones[:i] + [int(left), int(right)] + stones[i+1:]
            i += 1
        else:
            stones[i] *= 2024
        i += 1
        # print(stones)

# print(stones)
for i in range(1):
    blink()
    
print(f"Part 1: {len(stones)}")

# PART 2
stones = list(map(int, lines[0].split()))
mapping = defaultdict(int)
for s in stones:
    mapping[s] += 1

def blink():
    global stones
    keys = []
    old = mapping.copy()
    for v in mapping:
        if mapping[v] > 0:
            keys.append(v)

    for k in keys:
        cnt = old[k]
        res = calc(k)
        if type(res) == list:
            for r in res:
                mapping[r] += cnt
        else:
            mapping[res] += cnt
        mapping[k] -= cnt
        # print(stones)

def calc(n):
    size = len(str(n))
    if n == 0:
        return 1
    elif size % 2 == 0:
        left = str(n)[:size // 2]
        right = str(n)[size // 2:]
        return [int(left), int(right)]
    else:
        return n * 2024

for i in range(75):
    blink()

print(f"Part 2: {sum(mapping.values())}")
