## STARTER CODE
file = open('2015/Day01_data.txt', 'r')
data = file.read()

# PART 1

floor = 0
for c in data:
    match c:
        case '(': floor += 1
        case ')': floor -= 1

print(f"Part 1: {floor}")

# PART 2

floor = 0
for i in range(len(data)):
    if data[i] == '(':
        floor += 1
    elif data[i] == ')':
        floor -= 1
    if floor == -1:
        break

print(f"Part 2: {i + 1}")