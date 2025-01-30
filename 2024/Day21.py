## STARTER CODE
file = open('Day21_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
def hori(dc):
    c = ''
    if dc < 0:
        c += '>'*abs(dc)
    elif dc > 0:
        c += '<'*abs(dc)
    return c
def vert(dr):
    c = ''
    if dr > 0:
        c += '^'*abs(dr)
    elif dr < 0:
        c += 'v'*abs(dr)
    return c

numpad = {'7':(0, 0), '8':(0, 1), '9':(0, 2), '4':(1, 0), '5':(1, 1), '6':(1, 2), '1':(2, 0), '2':(2, 1), '3':(2, 2), '0':(3, 1), 'A':(3, 2)}
def num(code):
    curr = (3, 2)
    commands = ""
    for char in code:
        next = numpad[char]
        dr, dc = curr[0] - next[0], curr[1] - next[1]

        if curr[1] == 0:
            commands += hori(dc)
            commands += vert(dr)
        else:
            commands += vert(dr)
            commands += hori(dc)

        commands += 'A'
        curr = next
    return commands

keypad = {'^':(0, 1), 'A':(0, 2), '<':(1, 0), 'v':(1, 1), '>':(1, 2)}
def robot(code):
    curr = (0, 2)
    commands = ""
    for char in code:
        next = keypad[char]
        dr, dc = curr[0] - next[0], curr[1] - next[1]

        if curr[1] == 0:
            commands += hori(dc)
            commands += vert(dr)
        else:
            commands += vert(dr)
            commands += hori(dc)

        commands += 'A'
        curr = next
    return commands

codes = lines[:]
total = 0
for c in codes:
    comms = robot(robot(num(c)))
    print(c)
    print(num(c))
    print(robot(num(c)))
    print(comms)
    break
    total += len(comms) * int(c[:3])

print(f"Part 1: {total}")

# PART 2
