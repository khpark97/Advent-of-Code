## STARTER CODE
file = open('2015/Day05_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

bad = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
score = 0

def check_1(l):
    vowel = int(l[-1] in vowels)
    safe = False
    for i in range(len(l) - 1):
        if l[i:i+2] in bad:
            return 0
        if l[i] in vowels:
            vowel += 1
        if l[i] == l[i+1]:
            safe = True
    return safe and vowel >= 3
    
for l in lines:
    score += check_1(l)

print(f"Part 1: {score}")

# PART 2

score = 0
def check_2(l):
    repeat, pair = False, False
    seen = {}
    for i in range(len(l) - 1):
        if i < len(l) - 2 and l[i] == l[i+2]:
            repeat = True
        substr = l[i:i+2]
        if substr in seen:
            if (i - seen[substr]) > 1:
                pair = True
        else:
            seen[substr] = i
    return repeat and pair

for l in lines:
    score += check_2(l)

print(f"Part 2: {score}")