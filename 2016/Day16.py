## STARTER CODE
file = open('2016/Day16_data.txt', 'r')

# PART 1

initial = file.read()

def find_checksum(a, length):
    while len(a) < length:
        b = reversed(a)
        b = ''.join(['1' if i == '0' else '0' for i in b])
        a = ''.join([a, '0', b])
    
    checksum = a[:length]
    while len(checksum) % 2 == 0:
        i = 0
        res = []
        while i < len(checksum):
            if checksum[i] == checksum[i+1]:
                res.append('1')
            else:
                res.append('0')
            i += 2
        checksum = ''.join(res)
    return checksum

print(f"Part 1: {find_checksum(initial, 272)}")

# PART 2

print(f"Part 2: {find_checksum(initial, 35651584)}")