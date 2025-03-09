## STARTER CODE
file = open('2021/Day17_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

tx, ty = [[int(j) for j in i[2:].split('..')] for i in lines[0][13:].split(', ')]

def fire(vx, vy):
    x, y = [0, 0]
    high = 0
    while True:
        if x > tx[1] or y < ty[0]: 
            return -1
        high = max(high, y)
        if x >= tx[0] and y <= ty[1]:
            return high
        x += vx
        y += vy
        vx -= (vx > 0)
        vy -= 1

high = 0
valid = 0
for x in range(1, 1+tx[1]):
    for y in range(ty[0], -ty[0]):
        launch = fire(x, y)
        high = max(high, launch)
        if launch != -1:
            valid += 1
            
print(f"Part 1: {high}")

# PART 2

print(f"Part 2: {valid}")