## STARTER CODE
file = open('2017/Day01_data.txt', 'r')
data = file.read()

# PART 1

digits = [int(x) for x in data]
score = digits[0] if digits[0] == digits[-1] else 0
i = 0
while i < len(digits) - 1:
    if digits[i] == digits[i+1]:
        score += digits[i]
    i += 1

print(f"Part 1: {score}")

# PART 2

score = 0
halfway = int(len(digits) / 2)
for i in range(halfway):
    if digits[i] == digits[i + halfway]:
        score += digits[i] * 2

print(f"Part 2: {score}")