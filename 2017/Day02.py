## STARTER CODE
file = open('2017/Day02_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

p1 = 0
p2 = 0
for l in lines:
    digits = [int(x) for x in l.split()]
    p1 += max(digits) - min(digits)
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            high = max(digits[i], digits[j])
            low = min(digits[i], digits[j])
            if high % low == 0:
                p2 += high / low

print(f"Part 1: {p1}")

# PART 2

print(f"Part 2: {p2}")