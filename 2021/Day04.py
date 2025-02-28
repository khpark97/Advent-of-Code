## STARTER CODE
file = open('2021/Day04_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

order = [int(h) for h in lines[0].split(',')]

i = 2
boards = []
while i < len(lines):
    rows = []
    cols = []
    for j in range(i, i+5):
        rows.append([int(k) for k in lines[j].split()])
    for c in range(5):
        col = []
        for r in range(5):
            col.append(rows[r][c])
        cols.append(col)
    boards.append([rows, cols])
    i += 6

def call(n):
    for b in boards:
        rows, cols = b
        for i in range(len(rows)):
            if n in rows[i]:
                rows[i] = [-1 if x == n else x for x in rows[i]]
            if rows[i].count(-1) == 5:
                return b, n
        for j in range(len(cols)):
            if n in cols[j]:
                cols[j] = [-1 if x == n else x for x in cols[j]]
            if cols[j].count(-1) == 5:
                return b, n
    return b, -1

def bingo():
    for n in order:
        b, val = call(n)
        if val != -1:
            score = 0
            for r in b[0]:
                score += sum([0 if num == -1 else num for num in r])
            score *= val
            return score
            
score = bingo()

print(f"Part 1: {score}")

# PART 2

i = 2
boards = []
while i < len(lines):
    rows = []
    cols = []
    for j in range(i, i+5):
        rows.append([int(k) for k in lines[j].split()])
    for c in range(5):
        col = []
        for r in range(5):
            col.append(rows[r][c])
        cols.append(col)
    boards.append([rows, cols])
    i += 6

def call(n):
    val = -1
    finished = set()
    for i in range(len(boards)):
        rows, cols = boards[i]
        for j in range(len(rows)):
            if n in rows[j]:
                rows[j] = [-1 if x == n else x for x in rows[j]]
            if rows[j].count(-1) == 5:
                finished.add(i)
                val = n
        for k in range(len(cols)):
            if n in cols[k]:
                cols[k] = [-1 if x == n else x for x in cols[k]]
            if cols[k].count(-1) == 5:
                finished.add(i)
                val = n
    return finished, val

def bingo():
    global boards
    last = []
    for n in order:
        finished, val = call(n)
        if val != -1:
            temp = boards.copy()
            for b in finished:
                temp.remove(boards[b])
                last = boards[b]
            boards = temp
            if len(boards) == 0:
                break
    score = 0
    for r in last[0]:
        score += sum([0 if num == -1 else num for num in r])
    score *= val
    return score
            
score = bingo()

print(f"Part 2: {score}")