## STARTER CODE
file = open('2016/Day14_data.txt', 'r')
data = file.read()

# PART 1

import hashlib

secret_key = data

def find_keys(part):
    #check the next 1000 hexes in the cache
    def check(index, seq):
        for i in range(index+1, index+1000):
            if seq in cache[i]:
                return True
        return False

    def find_triples(string):
        for i in range(len(string) - 2):
            if string[i] == string[i+1] == string[i+2]:
                return string[i]
        return False
    
    i = 0
    keys = []
    cache = {}
    check_index, check_keys = 0, []
    while len(keys) < 64:
        key = f"{secret_key}{i}"
        hex = hashlib.md5(key.encode('utf-8')).hexdigest()
        if part == 2:
            for _ in range(2016):
                hex = hashlib.md5(hex.encode('utf-8')).hexdigest()
        cache[i] = hex
        triple = find_triples(hex)
        if triple:
            check_keys.append((i, triple * 5, hex))
        
        if len(check_keys) >= check_index + 1:
            curr = check_keys[check_index]
            if i == curr[0] + 1000:
                if check(curr[0], curr[1]):
                    keys.append((curr[0], curr[2]))
                check_index += 1
        i += 1
    return keys

print(f"Part 1: {find_keys(1)[63][0]}")

# PART 2

print(f"Part 2: {find_keys(2)[63][0]}")