## STARTER CODE
file = open('2015/Day11_data.txt', 'r')

# PART 1

pw = file.read()

def increment(curr):
    curr = list(curr)
    i = len(curr) - 1
    while i >= 0:
        if curr[i] == 'z':
            curr[i] = 'a'
            i -= 1
        else:
            curr[i] = chr(ord(curr[i]) + 1)
            break
    return ''.join(curr)

def next(curr):
    while True:
        curr = increment(curr)
        if any(['i', 'o', 'l']) in list(curr):
            continue

        three = False
        for i in range(len(curr) - 2):
            if ord(curr[i]) == ord(curr[i+1])-1 == ord(curr[i+2])-2:
                three = True
                break
        if not three:
            continue

        pair, j = 0, 0
        while j < len(curr) - 1:
            if curr[j] == curr[j+1]:
                pair += 1
                j += 1
            j += 1
        if pair < 2:
            continue

        return curr

pw = next(pw)

print(f"Part 1: {pw}")

# PART 2

pw = next(pw)

print(f"Part 2: {pw}")