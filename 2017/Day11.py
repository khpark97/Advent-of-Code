## STARTER CODE
file = open('2017/Day11_data.txt', 'r')
data = file.read()

# PART 1

steps = data.split(',')
curr = [0, 0]
furthest = -1
for step in steps:
    match step:
        case 'n':
            curr[1] += 2
        case 's':
            curr[1] -= 2
        case 'ne':
            curr[0] += 1
            curr[1] += 1
        case 'nw':
            curr[0] -= 1
            curr[1] += 1
        case 'se':
            curr[0] += 1
            curr[1] -= 1
        case 'sw':
            curr[0] -= 1
            curr[1] -= 1
    furthest = max(furthest, sum([abs(x) for x in curr])//2)

print(f"Part 1: {sum([abs(x) for x in curr])//2}")

# PART 2

print(f"Part 2: {furthest}")