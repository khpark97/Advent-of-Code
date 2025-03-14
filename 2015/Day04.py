## STARTER CODE
file = open('2015/Day04_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

import hashlib

secret_key = 'iwrupvqb'

parts = {'00000': float('inf'), '000000': float('inf')}

for start in ['00000', '000000']:
    i = 0
    key = secret_key + str(i)
    encoded_string = key.encode('utf-8')
    while not hashlib.md5(encoded_string).hexdigest().startswith(start):
        i += 1
        key = secret_key + str(i)
        encoded_string = key.encode('utf-8')
    parts[start] = i

print(f"Part 1: {parts['00000']}")

# PART 2

print(f"Part 2: {parts['000000']}")