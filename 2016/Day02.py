## STARTER CODE
file = open('2016/Day02_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

keypad_p1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r, c = 1, 1
result_p1 = []
for line in lines:
    for i in range(len(line)):
        match line[i]:
            case 'U': r = max(r-1, 0)
            case 'R': c = min(2, c+1)
            case 'D': r = min(r+1, 2)
            case 'L': c = max(c-1, 0)
    result_p1.append(str(keypad_p1[r][c]))

print(f"Part 1: {''.join(result_p1)}")

# PART 2

keypad_p2 = {(0, 2): 1, 
             (1, 1): 2, (1, 2): 3, (1, 3): 4,
             (2, 0): 5, (2, 1): 6, (2, 2): 7, (2, 3): 8, (2, 4): 9,
             (3, 1): 'A', (3, 2): 'B', (3, 3): 'C',
             (4, 2): 'D'}
result_p2 = []
dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
curr = (2, 0)
for line in lines:
    for i in range(len(line)):
        next = tuple(map(sum, zip(curr, dirs[line[i]])))
        if next in keypad_p2:
            curr = next
    r, c = curr
    result_p2.append(str(keypad_p2[(r, c)]))

print(f"Part 2: {''.join(result_p2)}")