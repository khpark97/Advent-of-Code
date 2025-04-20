## STARTER CODE
file = open('2017/Day09_data.txt', 'r')
stream = file.read()

# PART 1

score = 0
removed = 0
garbage = False
counter = 0
i = 0
while i < len(stream):
    curr = stream[i]
    if garbage:
        if curr == '>':
            garbage = False
        elif curr == '!':
            i += 1
        else:
            removed += 1

    elif not garbage:
        if curr == '{':
            counter += 1
        elif curr == '}':
            score += counter
            counter -= 1
        elif curr == '<':
            garbage = True

    i += 1

print(f"Part 1: {score}")

# PART 2

print(f"Part 2: {removed}")