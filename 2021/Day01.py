## STARTER CODE
file = open('2021/Day01_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

report = []
for l in lines:
    report.append(int(l))

total = 0
for i in range(len(report) - 1):
    if report[i] < report[i+1]:
        total += 1

print(f"Part 1: {total}")

# PART 2

total = 0
curr = sum(report[:2])
for i in range(len(report) - 3):
    next = curr - report[i] + report[i+3]
    if next > curr:
        total += 1
    curr = next

print(f"Part 2: {total}")