## STARTER CODE
file = open('2015/Day10_data.txt', 'r')
data = file.read()

# PART 1

res = data
def say(sequence):
    i = 0
    next = []
    while i < len(sequence):
        c = sequence[i]
        count = 0
        while i < len(sequence) and sequence[i] == c:
            count += 1
            i += 1
        next.append(str(count))
        next.append(c)
    return ''.join(next)

for _ in range(40):
    res = say(res)

print(f"Part 1: {len(res)}")

# PART 2

for _ in range(10):
    res = say(res)

print(f"Part 2: {len(res)}")