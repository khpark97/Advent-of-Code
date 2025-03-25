## STARTER CODE
file = open('2015/Day23_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

def program(a, b):
    registers = {'a': a, 'b': b}
    i = 0
    while i < len(lines):
        split = lines[i].split()
        command = split[0]
        match command:
            case 'hlf': registers[split[1]] //= 2
            case 'tpl': registers[split[1]] *= 3
            case 'inc': registers[split[1]] += 1
            case 'jmp': 
                i += int(split[1])
                continue
            case 'jie': 
                if registers[split[1].strip(',')] % 2 == 0:
                    i += int(split[2])
                    continue
            case 'jio': 
                if registers[split[1].strip(',')] == 1:
                    i += int(split[2])
                    continue
        i += 1
    return registers['b']

print(f"Part 1: {program(0, 0)}")

# PART 2

print(f"Part 2: {program(1, 0)}")