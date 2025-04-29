## STARTER CODE
file = open('2017/Day16_data.txt', 'r')
data = file.read()

# PART 1

import string
moves = data.split(',')
programs = [char for char in string.ascii_lowercase[:16]]

def dance(order):
    for move in moves:
        match move[0]:
            case 's': 
                spin = int(move[1:])
                order = order[-spin:] + order[:-spin]
            case 'x':
                p1, p2 = [int(x) for x in move[1:].split('/')]
                temp = order[p1]
                order[p1] = order[p2]
                order[p2] = temp
            case 'p':
                p1, p2 = [order.index(x) for x in move[1:].split('/')]
                temp = order[p1]
                order[p1] = order[p2]
                order[p2] = temp
    return order

danced = dance(programs.copy())

print(f"Part 1: {''.join(danced)}")

# PART 2


print(f"Part 2: {''.join(programs)}")