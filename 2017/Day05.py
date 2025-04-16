## STARTER CODE
file = open('2017/Day05_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

instructions = [int(x) for x in lines]
steps = 0
pointer = 0
while pointer < len(instructions):
    instructions[pointer] += 1
    pointer += instructions[pointer] - 1
    steps += 1

print(f"Part 1: {steps}")

# PART 2

instructions = [int(x) for x in lines]
steps = 0
pointer = 0
while pointer < len(instructions):
    offset = instructions[pointer]
    if instructions[pointer] >= 3:
        instructions[pointer] -= 1
    else:
        instructions[pointer] += 1
    pointer += offset
    steps += 1

print(f"Part 2: {steps}")