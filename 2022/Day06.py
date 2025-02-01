## STARTER CODE
file = open('2022/Day06_data.txt', 'r')
data = file.read()

# PART 1

i = 4
packet = data[:i]
chars = set(packet)
while len(chars) != 4:
    i += 1
    packet = data[i-4:i]
    chars = set(packet)

print(f"Part 1: {i}")

# PART 2

i = 14
packet = data[:i]
chars = set(packet)
while len(chars) != 14:
    i += 1
    packet = data[i-14:i]
    chars = set(packet)

print(f"Part 2: {i}")