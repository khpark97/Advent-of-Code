## STARTER CODE
file = open('2016/Day25_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

def run(a):
    result = []
    registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(lines):
        split = lines[i].split()
        x = split[1]
        match split[0]:
            case 'cpy':
                y = split[2]
                if x.isdigit():
                    registers[y] = int(x)
                else:
                    registers[y] = registers[x]
            case 'inc':
                registers[x] += 1
            case 'dec':
                registers[x] -= 1
            case 'jnz':
                y = int(split[2])
                if x in registers:
                    i += (y - 1) if registers[x] != 0 else 0
                elif x.isdigit():
                    i += (y - 1) if x != '0' else 0
            case 'out':
                if x in registers:
                    result.append(registers[x])
                else:
                    result.append(x)
        i += 1
        if len(result) == 12:
            return result

j = 0
while True:
    signal = run(j)
    if signal == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
        break
    j += 1

print(f"Part 1: {j}")

# PART 2

print(f"Part 2: {j}")