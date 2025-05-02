## STARTER CODE
file = open('2017/Day18_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

registers = {}
output = []
recovered = -1
i = 0

def command(registers, output, i):
    split = lines[i].split()

    x = split[1]
    if x not in registers:
        registers[x] = 0

    if len(split) > 2:
        y = split[2]
        if y.isalpha():
            if y in registers:
                y = registers[y]
            else:
                registers[y] = 0
                y = 0
        else:
            y = int(y)

    match split[0]:
        case 'set':
            registers[x] = y
        case 'add':
            registers[x] += y
        case 'mul':
            registers[x] *= y
        case 'mod':
            registers[x] %= y
        case _:
            if x.isalpha():
                x = registers[split[1]]
            else:
                x = int(split[1])
            match split[0]:
                case 'snd':
                    output.append(x)
                case 'rcv':
                    if x != 0:
                        return registers, output, i, output.pop()
                case 'jgz':
                    if x > 0:
                        i += y
                        return registers, output, i, -1
    i += 1
    return registers, output, i, -1

while i < len(lines):
    registers, output, i, recovered = command(registers, output, i)
    if recovered != -1:
        break

print(f"Part 1: {recovered}")

# PART 2

program_0 = {'p': 0}
program_1 = {'p': 1}
i_0 = 0
i_1 = 0
receive_0 = []
receive_1 = []
sent_1 = 0

while i_0 < len(lines) and i_1 < len(lines):
    split_0 = lines[i_0].split()
    split_1 = lines[i_1].split()

    terminate = 0
    if split_0[0] == 'rcv':
        if not receive_0:
            terminate += 1
        else:
            value = receive_0.pop(0)
            program_0[split_0[1]] = value
            i_0 += 1
    elif split_0[0] == 'snd':
        value = split_0[1]
        if value.isalpha():
            value = program_0[value]
        else:
            value = int(value)
        receive_1.append(value)
        i_0 += 1
    else:
        program_0, _, i_0, _ = command(program_0, None, i_0)

    if split_1[0] == 'rcv':
        if not receive_1:
            terminate += 1
        else:
            value = receive_1.pop(0)
            program_1[split_1[1]] = value
            i_1 += 1
    elif split_1[0] == 'snd':
        value = split_1[1]
        if value.isalpha():
            value = program_1[value]
        else:
            value = int(value)
        receive_0.append(value)
        sent_1 += 1
        i_1 += 1
    else:
        program_1, _, i_1, _ = command(program_1, None, i_1)

    if terminate == 2:
        break
    # print(i_0, i_1)

print(f"Part 2: {sent_1}")