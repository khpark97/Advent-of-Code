## STARTER CODE
file = open('2021/Day10_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
from collections import deque

part1 = 0
part2 = []
score1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
score2 = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
for i in range(len(lines)):
    q = deque()
    corrupt = False
    for c in lines[i]:
        if c in pairs.keys():
            q.append(c)
        else:
            last = q.pop()
            if pairs[last] != c:
                part1 += score1[c]
                corrupt = True
                break

    # PART 2
    if not corrupt:
        score = 0
        while q:
            last = q.pop()
            score *= 5
            score += score2[pairs[last]]
        part2.append(score)

print(f"Part 1: {part1}")

print(f"Part 2: {sorted(part2)[len(part2)//2]}")