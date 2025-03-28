## STARTER CODE
file = open('2016/Day06_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import defaultdict, Counter
chars = defaultdict(list)
for l in lines:
    for i in range(len(l)):
        chars[i].append(l[i])

most = []
least = []
for col in chars:
    count = Counter(chars[col])
    most.append(count.most_common(1)[0][0])
    least.append(count.most_common()[-1][0])

print(f"Part 1: {''.join(most)}")

# PART 2

print(f"Part 2: {''.join(least)}")