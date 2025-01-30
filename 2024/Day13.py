## STARTER CODE
file = open('Day13_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
button_a, button_b, prizes = [], [], []
for i in range(0, len(lines), 4):
    button_a.append([int(k.split('+')[1]) for k in lines[i][10:].split(', ')])
    button_b.append([int(k.split('+')[1]) for k in lines[i+1][10:].split(', ')])
    prizes.append([int(k.split('=')[1]) for k in lines[i+2][7:].split(', ')])
# print(button_a, button_b, prizes)

tokens = 0
for j in range(len(button_a)):
    a, b, p = button_a[j], button_b[j], prizes[j]
    A = (p[0]*b[1] - p[1]*b[0]) // (a[0]*b[1] - a[1]*b[0])
    B = (a[0]*p[1] - a[1]*p[0]) // (a[0]*b[1] - a[1]*b[0])
    if A*a[0] + B*b[0] == p[0] and A*a[1] + B*b[1] == p[1]:
        tokens += A*3 + B
        
print(f"Part 1: {tokens}")

# PART 2
tokens = 0
for j in range(len(button_a)):
    a, b = button_a[j], button_b[j]
    p = [p + 10000000000000 for p in prizes[j]]
    A = (p[0]*b[1] - p[1]*b[0]) // (a[0]*b[1] - a[1]*b[0])
    B = (a[0]*p[1] - a[1]*p[0]) // (a[0]*b[1] - a[1]*b[0])
    if A*a[0] + B*b[0] == p[0] and A*a[1] + B*b[1] == p[1]:
        tokens += A*3 + B
        
print(f"Part 2: {tokens}")