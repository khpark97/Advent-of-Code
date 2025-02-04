## STARTER CODE
file = open('2022/Day09_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

p1, p2 = set([(0, 0)]), set([(0, 0)])
rope = [(0, 0)] * 10
dirs = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}

def tail(h, t):
    dr = h[0] - t[0]
    dc = h[1] - t[1]

    if abs(dr) > 1 or abs(dc) > 1:
        if dr != 0:
            t = (t[0] + (1 if dr > 0 else -1), t[1])
        if dc != 0:
            t = (t[0], t[1] + (1 if dc > 0 else -1))

    return t

for line in lines:
    d, move = line.split()
    # print(d, move)
    for m in range(int(move)):
        rope[0] = tuple(map(sum, zip(rope[0], dirs[d])))
        for i in range(9):
            rope[i+1] = tail(rope[i], rope[i+1])
        p1.add(rope[1])
        p2.add(rope[9])
        
print(f"Part 1: {len(p1)}")

# PART 2

print(f"Part 2: {len(p2)}")