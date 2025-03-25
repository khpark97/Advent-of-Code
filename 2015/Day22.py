## STARTER CODE
file = open('2015/Day22_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import re
boss = [int(x) for x in re.findall(r'\d+', ''.join(lines))]
b_hp = boss[0]
b_dmg = boss[1]

# player = [50, 0, 500]
# least = float('inf')
# most = 0

# def cast(p, b_hp, spells):
#     resulting_spells = []
#     p_hp, p_armor, p_mana = p
#     p_armor = 0
#     for spell, count in spells:
#         match spell:
#             case 's': p_armor = 7
#             case 'p': b_hp -= 3
#             case 'r': p_mana += 101
#         if count > 1:
#             resulting_spells.append((spell, count - 1))
#     return p_hp, p_armor, p_mana, b_hp, resulting_spells

# def choose_spell(mana, b_hp):
#     resulting_spells = []
#     return mana

# from collections import deque
# q = deque([(player, b_hp, 0, [])]) #player, boss, spent, active spells
# while q:
#     p, b_hp, spent, active_spells = q.popleft()
#     p_hp, p_armor, p_mana = p

#     p_hp, p_armor, p_mana, b_hp, active_spells = cast(p, b_hp, active_spells)
#     p_mana, b_hp, active_spells = choose_spell(p_mana, b_hp)

#     if b_hp <= 0:
#         least = min(least, spent)
#         continue
    
#     p_hp, p_armor, p_mana, b_hp, active_spells = cast(p, b_hp, active_spells)

#     p_hp -= max(1, b_dmg - p_armor)
#     if p_hp <= 0:
#         most = max(most, spent)
#         continue
#     q.append(((p_hp, p_armor, p_mana), b_hp, spent, active_spells))

# print(f"Part 1: {least}")

# # PART 2

# print(f"Part 2: {most}")



class Wizard:
    def __init__(self, player: list, boss: list):
        p_hp, p_armor, p_mana = player
        self.p_hp = p_hp
        self.p_armor = p_armor
        self.p_mana = p_mana
        
        b_hp, b_dmg = boss
        self.b_hp = b_hp
        self.b_dmg = b_dmg

        self.mana_spent = 0
        self.active = []

    def cast(self, spells):
        result = []
        self.p_armor = 0
        for spell, count in spells:
            match spell:
                case 's': self.p_armor = 7
                case 'p': self.b_hp -= 3
                case 'r': self.p_mana += 101
            if count > 1:
                result.append((spell, count - 1))
        self.active = result

    def immediate(self, spell):
        match spell:
            case 'm': self.b_hp -= 4
            case 'd':
                self.b_hp -= 2
                self.p_hp += 2
        
    def choose_spell(self, prompt: str) -> str:
        try:
            i = input(prompt)
        except ValueError:
            print("Invalid input. Please enter a valid spell amongst m, d, s, p, r.")
        if i in ['m', 'd']:
            self.immediate(i)
        else:
            counts = {'s': 6, 'p': 6, 'r': 5}
            self.active.append((i, counts[i]))

    def choose(self):
        if self.p_mana < 53:
            return -1

    def turn(self):
        self.cast()
        if self.b_hp <= 0:
            # least = min(least, self.mana_spent)
            return 1
        
        self.cast()
        self.p_hp -= max(1, self.b_dmg - self.p_armor)
        if self.p_hp <= 0:
            # most = max(most, self.mana_spent)
            return -1

if __name__ == "__main__":
    player = [50, 0, 500]
    game = Wizard(player, boss)
    while True:
        game.turn()