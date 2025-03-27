## STARTER CODE
file = open('2016/Day04_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import Counter
total = 0

def decrypt(name, id):
    result = []
    id %= 26
    for n in name:
        decrypted = []
        for c in n:
            decrypted.append(chr((ord(c) - ord('a') + id) % 26 + ord('a')))
        result.append(''.join(decrypted))
        result.append(' ')
    return ''.join(result[:-1])

names = []

for l in lines:
    partition = l.rsplit("[", 1)
    checksum = partition[1].strip(']')
    split = partition[0].split('-')
    id = split[-1]
    chars = ''.join(split[:-1])
    
    count = Counter(chars).items()
    count = sorted(count, key=lambda x: (-x[1], x[0]))
    if all([checksum[i] == count[i][0] for i in range(len(checksum))]):
        total += int(id)
        names.append((decrypt(split[:-1], int(id)), id))

print(f"Part 1: {total}")

# PART 2

part_2 = 0
for name, id in names:
    if "northpole" in name:
        part_2 = id
        break

print(f"Part 2: {part_2}")