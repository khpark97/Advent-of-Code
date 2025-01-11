## STARTER CODE
file = open('Day3_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
total = 0
for l in lines:
    i = 0
    while i != -1:
        i = l.find("mul(")
        section = l[i+4:min(len(l), i+12)]
        split = section.split(",")
        if split[0].isdigit() and len(split[0]) <= 3:
            end = split[1].find(')')
            if end != -1:
                right = split[1][:end]
                if right.isdigit():
                    left = int(split[0])
                    total += left * int(right)
        l = l[min(len(l), i+4):]
print(total)

# PART 2
total = 0
for l in lines:
    i = 0
    while i != -1:
        i = l.find("mul(")
        dont = l.find("don't()")
        if dont != -1 and dont < i:
            do = l.find("do()")
            if do == -1:
                break
            l = l[min(len(l), do+4):]
            continue
        section = l[i+4:min(len(l), i+12)]
        split = section.split(",")
        if split[0].isdigit() and len(split[0]) <= 3:
            end = split[1].find(')')
            if end != -1:
                right = split[1][:end]
                if right.isdigit():
                    left = int(split[0])
                    total += left * int(right)
        l = l[min(len(l), i+4):]
print(total)