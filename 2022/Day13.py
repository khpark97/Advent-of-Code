## STARTER CODE
file = open('2022/Day13_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

left, right = [], []
i = 0
while i < len(lines):
    left.append(eval(lines[i]))
    right.append(eval(lines[i+1]))
    i += 3
    
def compare(l, r):
    j = 0
    while j < max(len(l), len(r)):
        if j >= len(l):
            return True
        elif j >= len(r):
            return False
        if type(l[j]) == int and type(r[j]) == int:
            if r[j] < l[j]:
                return False
            elif l[j] < r[j]:
                return True
        elif type(l[j]) == int and type(r[j]) == list:
            comp = compare([l[j]], r[j])
            if comp != -1:
                return comp
        elif type(l[j]) == list and type(r[j]) == int:
            comp = compare(l[j], [r[j]])
            if comp != -1:
                return comp
        else:
            comp = compare(l[j], r[j])
            if comp != -1:
                return comp
        j += 1
    return -1

score = 0
for p in range(len(left)):
    if compare(left[p], right[p]) == True:
        score += p + 1

print(f"Part 1: {score}")

# PART 2



print(f"Part 2: {score}")