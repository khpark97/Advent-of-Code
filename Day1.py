## STARTER CODE
file = open('Day1_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import defaultdict

# PART 1
list1, list2 = [], []
for l in lines:
    nums = l.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))
list1 = sorted(list1)
list2 = sorted(list2)
total = 0
for i in range(len(list1)):
    total += abs(list2[i] - list1[i])
print(total)

# PART 2
seen1, seen2 = defaultdict(int), defaultdict(int)
for l in lines:
    nums = l.split()
    seen1[int(nums[0])] += 1
    seen2[int(nums[1])] += 1
similarity = 0
print(len(seen1), len(seen2))
for num in seen1:
    similarity += (num * seen2[num])
print(similarity)