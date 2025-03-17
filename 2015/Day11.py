## STARTER CODE
file = open('2015/Day11_data.txt', 'r')

# PART 1

pw = file.read()

def increment(curr):
    if curr[-1] == 'z':
        return increment(curr[:-1]) + 'a'
    return curr[:-1] + chr((ord(curr[-1]) - 70) % 26 + 97)

def next(curr):
    curr = increment(curr)
    while True:
        if any(['i', 'o', 'l']) in list(curr):
            curr = increment(curr)
            continue

        three = False
        for i in range(len(curr) - 2):
            if ord(curr[i]) == ord(curr[i+1])-1 == ord(curr[i+2])-2:
                three = True
        if not three:
            curr = increment(curr)
            continue

        pair, j = 0, 0
        while j < len(curr) - 1:
            if curr[j] == curr[j+1]:
                pair += 1
                j += 1
            j += 1
        if pair < 2:
            curr = increment(curr)
            continue

        return curr

pw = next(pw)

print(f"Part 1: {pw}")

# PART 2

pw = next(pw)

print(f"Part 2: {pw}")