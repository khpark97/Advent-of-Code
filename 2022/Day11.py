## STARTER CODE
file = open('2022/Day11_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import deque
import heapq

monkeys = {}
i = 0
while i < len(lines):
    num = int(lines[i].split()[1][0])
    items = deque([int(x) for x in lines[i+1][18:].split(', ')])
    op = lines[i+2][13:].split()[-2:]
    div = int(lines[i+3].split()[-1])
    t = int(lines[i+4].split()[-1])
    f = int(lines[i+5].split()[-1])
    monkeys[num] = [items, op, div, t, f]
    i += 7

active = [0] * len(monkeys)

def round():
    for j in monkeys:
        items, op, div, t, f = monkeys[j]
        active[j] += len(items)
        while items:
            item = items.popleft()
            o, val = op
            if val == 'old':
                val = item
            if o == '+':
                item += int(val)
            else:
                item *= int(val)
            item //= 3
            if item % div == 0:
                monkeys[t][0].append(item)
            else:
                monkeys[f][0].append(item)

for k in range(20):
    round()
    # for m in monkeys:
    #     print(f"Monkey {m}: {monkeys[m][0]}")
    
business = heapq.nlargest(2, active)

print(f"Part 1: {business[0] * business[1]}")

# PART 2

monkeys = {}
i = 0
modulo = 1
while i < len(lines):
    num = int(lines[i].split()[1][0])
    items = deque([int(x) for x in lines[i+1][18:].split(', ')])
    op = lines[i+2][13:].split()[-2:]
    div = int(lines[i+3].split()[-1])
    t = int(lines[i+4].split()[-1])
    f = int(lines[i+5].split()[-1])
    monkeys[num] = [items, op, div, t, f]
    i += 7
    modulo *= div

active = [0] * len(monkeys)

def round():
    for j in monkeys:
        items, op, div, t, f = monkeys[j]
        active[j] += len(items)
        while items:
            item = items.popleft()
            o, val = op
            if val == 'old':
                val = item
            if o == '+':
                item += int(val)
            else:
                item *= int(val)
            item %= modulo
            if item % div == 0:
                monkeys[t][0].append(item)
            else:
                monkeys[f][0].append(item)

for k in range(10000):
    round()
    # for m in monkeys:
    #     print(f"Monkey {m}: {monkeys[m][0]}")
    
business = heapq.nlargest(2, active)

print(f"Part 2: {business[0] * business[1]}")