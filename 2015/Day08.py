## STARTER CODE
file = open('2015/Day08_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

part1 = 0
for l in lines:
    escape = 0
    i = 1
    while i < len(l) - 1:
        pair = l[i:i+2]
        if pair == '\\\"' or pair == '\\\\':
            escape += 1
            i += 1
        elif pair == '\\x':
            escape += 1
            i += 3
        else:
            escape += 1
        i += 1
    part1 += len(l) - escape

print(f"Part 1: {part1}")

# PART 2

part2 = 0
for l in lines:
    literal = 2
    for char in l:
        if char == '\"' or char == '\\': 
            literal += 1
    part2 += literal

print(f"Part 2: {part2}")