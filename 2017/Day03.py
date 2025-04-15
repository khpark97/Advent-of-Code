## STARTER CODE
file = open('2017/Day03_data.txt', 'r')
square = int(file.read())

# PART 1

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

grid = [[0 for _ in range(1000)] for _ in range(1000)]
grid[500][500] = 1
curr = (500, 500)
end = (-1, -1)

def add_layer(side_len, part):
    global curr
    cr, cc = curr
    curr_val = grid[cr][cc]
    curr = (cr + 1, cc + 1)
    for d in dirs:
        for _ in range(side_len):
            cr, cc = tuple(map(sum, zip(curr, d)))
            if part == 1:
                curr_val += 1
                if curr_val == square:
                    return (cr, cc)
            elif part == 2:
                curr_val = 0
                for adj in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]:
                    nr, nc = tuple(map(sum, zip((cr, cc), adj)))
                    curr_val += grid[nr][nc]
                if curr_val > square:
                    return curr_val
            grid[cr][cc] = curr_val
            curr = (cr, cc)
    return (-1, -1)

side_len = 2
while end == (-1, -1):
    end = add_layer(side_len, 1)
    side_len += 2

start = (500, 500)
dist = sum([abs(start[i] - end[i]) for i in [0, 1]])

print(f"Part 1: {dist}")

# PART 2

grid = [[0 for _ in range(1000)] for _ in range(1000)]
grid[500][500] = 1
curr = (500, 500)
end = (-1, -1)

side_len = 2
while end == (-1, -1):
    end = add_layer(side_len, 2)
    side_len += 2

print(f"Part 2: {end}")