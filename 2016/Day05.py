## STARTER CODE
file = open('2016/Day05_data.txt', 'r')
data = file.read()

# PART 1

import hashlib

secret_key = data

res_p1 = []
res_p2 = [-1 for _ in range(8)]
i = -1
while -1 in res_p2:
    i += 1
    key = secret_key + str(i)
    encoded_string = key.encode('utf-8')
    hex = hashlib.md5(encoded_string).hexdigest()
    while not hex.startswith('00000'):
        i += 1
        key = secret_key + str(i)
        encoded_string = key.encode('utf-8')
        hex = hashlib.md5(encoded_string).hexdigest()
    res_p1.append(hex[5])
    if hex[5].isdigit() and int(hex[5]) in range(8):
        pos = int(hex[5])
        if res_p2[pos] == -1:
            res_p2[pos] = hex[6]
    print(hex, res_p1, res_p2)

print(f"Part 1: {''.join(res_p1[:8])}")

# PART 2

print(f"Part 2: {''.join(res_p2)}")