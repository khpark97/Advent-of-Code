## STARTER CODE
file = open('Day9_data', 'r')
data = file.read()

# PART 1
files, spaces = [], []
for i in range(len(data)):
    if i % 2 == 0:
        files.append(int(data[i]))
    else:
        spaces.append(int(data[i]))
# print(data, files, spaces)

left = 0
right = len(data)//2
id = 0
checksum = 0
while left < len(files):
    if files[left] != 0:
        checksum += left * (((files[left]-1) * ((files[left]-1) + 1) // 2) + (id * files[left]))
        id += files[left]
        files[left] = 0
        # print(checksum)
    # while files[left] != 0:
    #     if sum(files) == 0:
    #         break
    #     # print('left', files, spaces)
    #     checksum += id * left
    #     id += 1
    #     files[left] -= 1
    while left < len(spaces) and spaces[left] != 0:
        if sum(files) == 0:
            break
        # print('right', files, spaces)
        checksum += id * right
        # print(checksum)
        id += 1
        files[right] -= 1
        spaces[left] -= 1
        if files[right] == 0:
            right -= 1
    left += 1
print(f"Part 1: {checksum}")

# PART 2
files, spaces, size = [], [], 0
for i in range(len(data)):
    d = int(data[i])
    if i % 2 == 0:
        files.append(size)
        files.append(d)
    else:
        spaces.append(size)
        spaces.append(d)
    size += d
# print(files, spaces)

id = 0
left = 1
system = []
while left < len(files):
    for i in range(files[left]):
        system.append(id)
    if left < len(spaces):
        for j in range(spaces[left]):
            system.append('.')
    id += 1
    left += 2

id = 2
size = len(data) // 2
for j in range(len(files)-1, 1, -2):
    for i in range(1, min(j, len(spaces)), 2):
        if files[j] > 0 and files[j] <= spaces[i]:
            # print(system)
            right = system.index(j//2)
            system[spaces[i-1]:spaces[i-1]+files[j]] = system[right:right+files[j]]
            system[right:right+files[j]] = ['.'] * files[j]
            spaces[i] -= files[j]
            spaces[i-1] += files[j]
            id += files[j]
            files[j] = 0
            break
# print(system)

checksum = 0
for k in range(len(system)):
    if system[k] != '.':
        checksum += k * system[k]
print(f"Part 2: {checksum}")
# print(data, files, spaces)

# print(system)
# space, right = 0, len(data)//2
# id = 0
# checksum = 0
# seen = set()
# while id < size:
#     print(id)
#     if system[id] == '.':
#         ptr = right
#         while ptr > 0:
#             last = files[ptr]
#             for i in range(len(spaces)):
#                 if last > 0 and spaces[i] >= last:
#                     seen.add(ptr)
#                     for j in range(last):
#                         checksum += id * ptr
#                         id += 1
#                         spaces[i] -= 1
#                         files[ptr] -= 1
#                     right -= 1
#                     break
#             ptr -= 1
#         id += 1
#     else:
#         if system[id] not in seen:
#             checksum += id * system[id]
#         id += 1
# print(seen, spaces, files)
