## STARTER CODE
file = open('2016/Day23_data.txt', 'r')
data = file.read()
commands = data.splitlines()

# PART 1

def run(a, b, c, d):
    lines = commands.copy()
    registers = {'a': a, 'b': b, 'c': c, 'd': d}
    i = 0
    while i < len(lines):
        split = lines[i].split()
        x = split[1]
        match split[0]:
            case 'tgl':
                jump = i + registers[x]
                if jump < len(lines):
                    cmd = lines[jump]
                    match cmd.split()[0]:
                        case 'cpy':
                            lines[jump] = 'jnz' + lines[jump][3:]
                        case 'inc':
                            lines[jump] = 'dec' + lines[jump][3:]
                        case 'jnz':
                            lines[jump] = 'cpy' + lines[jump][3:]
                        case _:
                            lines[jump] = 'inc' + lines[jump][3:]

            case 'cpy':
                y = split[2]
                if x in registers:
                    registers[y] = registers[x]
                else:
                    registers[y] = int(x)

            case 'inc':
                registers[x] += 1
            case 'dec':
                registers[x] -= 1

            case 'jnz':
                arg = split[2]
                y = registers[arg] if arg in registers else int(arg)
                if x in registers:
                    i += (y - 1) if registers[x] != 0 else 0
                elif x.isdigit():
                    i += (y - 1) if x != '0' else 0

            case 'skip':
                pass
        i += 1
        # print(registers, i)
    return registers

print(f"Part 1: {run(7, 0, 0, 0)['a']}")

# PART 2

# print(f"Part 2: {run(12, 0, 0, 0)['a']}")