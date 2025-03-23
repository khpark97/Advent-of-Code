## STARTER CODE
file = open('2015/Day21_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
boss = [int(x) for x in re.findall(r'\d+', ''.join(lines[:3]))]

def battle(player, boss):
    p_hp, p_dmg, p_armor = player
    b_hp, b_dmg, b_armor = boss
    while True:
        b_hp -= max(1, (p_dmg - b_armor))
        if b_hp <= 0:
            return 1
        p_hp -= max(1, (b_dmg - p_armor))
        if p_hp <= 0:
            return -1
        
store = {'weapons': [(int(a), int(b), int(c)) for (a, b, c) in [re.findall(r'\d+', l) for l in lines[5:10]]],
         'armors': [(int(a), int(b), int(c)) for (a, b, c) in [re.findall(r'\d+', l) for l in lines[12:17]]],
         'rings': [(int(a), int(b), int(c)) for (_, a, b, c) in [re.findall(r'\d+', l) for l in lines[19:25]]]}

from itertools import combinations, chain, product

weapons = list(chain.from_iterable((combinations(store['weapons'], r) for r in range(1, 2))))
armors = list(chain.from_iterable((combinations(store['armors'], r) for r in range(2))))
rings = list(chain.from_iterable((combinations(store['rings'], r) for r in range(3))))

products = list(product(weapons, armors, rings))
possibilities = [(*x, *y, *z) for x, y, z in products]

least = float('inf')
most = 0
for p in possibilities:
    player = [100, 0, 0]
    spent = 0
    for item in p:
        cost, dmg, armor = item
        spent += cost
        player[1] += dmg
        player[2] += armor
    result = battle(player, boss)
    if result == 1:
        least = min(least, spent)
    elif result == -1:
        most = max(most, spent)

print(f"Part 1: {least}")

# PART 2

print(f"Part 2: {most}")