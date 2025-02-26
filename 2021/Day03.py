## STARTER CODE
file = open('2021/Day03_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

bits = [0] * len(lines[0])
for line in lines:
    for i in range(len(line)):
        bits[i] += int(line[i])

res = ''
for b in bits:
    if b > len(lines)//2:
        res += '1'
    else:
        res += '0'
        
n = '1'*len(bits)

print(f"Part 1: {int(res, 2) * (~int(res, 2) & int('0b'+n,2))}")

# PART 2

bits = [0] * len(lines[0])
oxygen = []
temp = lines.copy()
for i in range(len(bits)):
    for j in range(len(temp)):
        bits[i] += int(temp[j][i])
    if bits[i] >= len(temp)/2:
        curr = '1'
    else:
        curr = '0'
    new = []
    for j in range(len(temp)):
        if temp[j][i] == curr:
            new.append(temp[j])
    temp = new
    oxygen.append(curr)
   
bits = [0] * len(lines[0]) 
co2 = []
temp = lines.copy()
for i in range(len(bits)):
    if len(temp) == 1:
        while i < len(temp[0]):
            co2.append(temp[0][i])
            i += 1
        break
    for j in range(len(temp)):
        bits[i] += int(temp[j][i])
    if bits[i] >= len(temp)/2:
        curr = '0'
    else:
        curr = '1'
    new = []
    for j in range(len(temp)):
        if temp[j][i] == curr:
            new.append(temp[j])
    temp = new
    co2.append(curr)
    
print(f"Part 2: {int(''.join(oxygen), 2) * int(''.join(co2), 2)}")