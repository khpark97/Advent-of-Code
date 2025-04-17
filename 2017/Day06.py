## STARTER CODE
file = open('2017/Day06_data.txt', 'r')
data = file.read()

# PART 1

banks = [int(x) for x in data.split()]
seen = {tuple(banks): 0}

def redistribute(config):
    most = max(config)
    index = config.index(most)
    config[index] = 0
    for bank in range(index+1, index+1+most):
        i = bank % len(config)
        config[i] += 1
    return config

cycles = 0
while True:
    banks = redistribute(banks)
    cycles += 1
    if tuple(banks) in seen:
        break
    seen[tuple(banks)] = cycles

print(f"Part 1: {cycles}")

# PART 2

print(f"Part 2: {cycles - seen[tuple(banks)]}")