## STARTER CODE
file = open('2022/Day02_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
score = 0
for round in lines:
    o, p = round.split()
    match o:
        case 'A':
            match p:
                case 'X': score += 4
                case 'Y': score += 8
                case 'Z': score += 3
        case 'B':
            match p:
                case 'X': score += 1
                case 'Y': score += 5
                case 'Z': score += 9
        case 'C':
            match p:
                case 'X': score += 7
                case 'Y': score += 2
                case 'Z': score += 6

print(f"Part 1: {score}")

# PART 2
score = 0
for round in lines:
    o, p = round.split()
    match o:
        case 'A':
            match p:
                case 'X': score += 3
                case 'Y': score += 4
                case 'Z': score += 8
        case 'B':
            match p:
                case 'X': score += 1
                case 'Y': score += 5
                case 'Z': score += 9
        case 'C':
            match p:
                case 'X': score += 2
                case 'Y': score += 6
                case 'Z': score += 7

print(f"Part 2: {score}")