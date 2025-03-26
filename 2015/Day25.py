## STARTER CODE
file = open('2015/Day25_data.txt', 'r')
data = file.read()

# PART 1

import re
row, col = [int(x) for x in re.findall(r'\d+', data)]

def calculate(r, c):
    start = 20151125
    cr, cc = 1, 1
    while True:
        if cr == r and cc == c:
            return start
        if cr == 1:
            cr = cc + 1
            cc = 1
        else:
            cr -= 1
            cc += 1
        start *= 252533
        start %= 33554393

print(f"Part 1: {calculate(row, col)}")

# PART 2

# print(f"Part 2: {calculate(row, col)}")