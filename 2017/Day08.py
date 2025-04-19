## STARTER CODE
file = open('2017/Day08_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

registers = {}
highest = -1
for l in lines:
    r, operand, amount, _, *condition = l.split()
    con_r = condition[0]
    if con_r not in registers:
        registers[con_r] = 0
    condition[0] = registers[con_r]
    if r not in registers:
        registers[r] = 0
    if eval(''.join([str(x) for x in condition])):
        match operand:
            case 'inc':
                registers[r] += int(amount)
            case 'dec':
                registers[r] -= int(amount)
    highest = max(highest, max(registers.values()))

print(f"Part 1: {max(registers.values())}")

# PART 2

print(f"Part 2: {highest}")