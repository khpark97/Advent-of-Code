## STARTER CODE
file = open('2016/Day12_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

def run(a, b, c, d):
    registers = {'a': a, 'b': b, 'c': c, 'd': d}
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
        i += 1
    return registers

print(f"Part 1: {run(0, 0, 0, 0)['a']}")

# PART 2

print(f"Part 2: {run(0, 0, 1, 0)['a']}")