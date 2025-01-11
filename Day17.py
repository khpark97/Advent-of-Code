## STARTER CODE
file = open('Day17_data', 'r')
data = file.read()
lines = data.splitlines()

from collections import deque

# PART 1
registers = [int(lines[i][12:]) for i in range(3)]
program = [int(i) for i in lines[-1][9:].split(',')]
# print(registers, program)

def run():
    result = []
    i = 0
    while i < len(program):
        # print(i, registers)
        opcode = program[i]
        operand = program[i+1]
        def combo(o):
            if o in range(4, 7):
                return registers[o-4]
            return o
        # print(registers, opcode, operand)
        match opcode:
            case 0: registers[0] = registers[0]//(2**combo(operand))
            case 1: registers[1] ^= operand
            case 2: registers[1] = combo(operand) % 8
            case 3:
                if registers[0] != 0:
                    i = operand
                    continue
            case 4: registers[1] ^= registers[2]
            case 5: result.append(str(combo(operand)%8))
            case 6: registers[1] = registers[0]//(2**combo(operand))
            case 7: registers[2] = registers[0]//(2**combo(operand))
        i += 2
    return result

print(f"Part 1: {','.join(run())}")

# PART 2
q = deque()
q.append((8**15, 1))
state = 0
low = float("inf")
while q:
    j, pointer = q.popleft()
    # print(j, pointer)
    for mult in range(0, 8):
        value = j + 8**(16-pointer) * mult
        registers[0] = value
        state = [int(i) for i in run()]
        if state == program:
            low = min(low, value)
        elif state[-pointer:] == program[-pointer:]:
            q.append((value, pointer+1))

print(f"Part 2: {low}")