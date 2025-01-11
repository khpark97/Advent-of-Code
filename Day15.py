## STARTER CODE
file = open('Day15_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
board = []
moves = ''
pos = ()
for i in range(len(lines)):
    if not lines[i]:
        continue
    elif lines[i][0] == '#':
        if '@' in lines[i]:
            start = lines[i].index('@')
            board.append(lines[i][:start] + '.' + lines[i][start+1:])
            pos = (i, start)
        else:
            board.append(lines[i])
    else:
        moves += lines[i]
# print(board, moves, pos)

def move(dir):
    global pos
    r, c = tuple(map(sum, zip(pos, dir)))
    next = board[r][c]
    # print(pos, next)
    if next == '.':
        pos = (r, c)
    elif next == 'O':
        temp = r, c
        while next == 'O':
            r, c = tuple(map(sum, zip((r, c), dir)))
            next = board[r][c]
            if next == '.':
                board[r] = board[r][:c] + 'O' + board[r][c+1:]
                tr, tc = temp
                board[tr] = board[tr][:tc] + '.' + board[tr][tc+1:]
                pos = (tr, tc)
    
for m in moves:
    match m:
        case '^':
            dir = (-1, 0)
        case '>':
            dir = (0, 1)
        case '<':
            dir = (0, -1)
        case 'v':
            dir = (1, 0)
    # print(m)
    move(dir)

gps = 0
for r in range(1, len(board) - 1):
    for c in range(1, len(board[0]) - 1):
        if board[r][c] == 'O':
            gps += c + r*100

print(f"Part 1: {gps}")

# PART 2
board = []
moves = ''
pos = ()
i = 0
while True:
    line = ''
    for c in lines[i]:
        match c:
            case '#':
                line += '##'
            case 'O':
                line += '[]'
            case '.':
                line += '..'
            case '@':
                line += '@'
                pos = (i, line.index('@'))
                line = line[:-1] + '..'
    board.append(line)
    i += 1
    if not lines[i]:
        i += 1
        break
while i < len(lines):
    moves += lines[i]
    i += 1
# print(board, pos)
    
boxes = set()
def move(dir):
    global pos, boxes
    r, c = tuple(map(sum, zip(pos, dir)))
    next = board[r][c]
    # print(pos, next)
    # for l in board:
    #     print(l)
    if next == '.':
        pos = (r, c)
    elif next == '[' or next == ']':
        if dir[0] == 0:
            temp = c
            while next == '[' or next == ']':
                c += dir[1]
                next = board[r][c]
                if next == '.':
                    # for l in board:
                    #     print(l)
                    tc = temp
                    if dir[1] == -1:
                        board[r] = board[r][:c] + board[r][c+1:tc+1] + '.' + board[r][tc+1:]
                    else:
                        board[r] = board[r][:tc] + '.' + board[r][tc:c] + board[r][c+1:]
                    pos = (r, tc)
                    # for l in board:
                    #     print(l)
        else:
            boxes.clear()
            if next == '[':
                mov = box(dir, (r, c)) and box(dir, (r, c+1))
            else:
                mov = box(dir, (r, c)) and box(dir, (r, c-1))
            if mov:
                pos = (r, c)
                for b, r, c in boxes:
                    board[r] = board[r][:c] + '.' + board[r][c+1:]
                for b, r, c in boxes:
                    board[r+dir[0]] = board[r+dir[0]][:c] + b + board[r+dir[0]][c+1:]
    # for l in board:
    #     print(l)

def box(dir, coords):
    cr, cc = coords
    curr = board[cr][cc]
    if curr == '[' or curr == ']':
        boxes.add((curr, cr, cc))
    r, c = tuple(map(sum, zip(dir, coords)))
    next = board[r][c]
    if next == '[' or next == ']':
        boxes.add((next, r, c))
    if next == '.':
        return True
    elif next == '[':
        if next == curr:
            if box(dir, (r, c)):
                return True
        else:
            if box(dir, (r, c)) and box(dir, (r, c+1)):
                return True
    elif next == ']':
        if next == curr:
            if box(dir, (r, c)):
                return True
        else:
            if box(dir, (r, c)) and box(dir, (r, c-1)):
                return True
    return False

i = 0
for m in moves:
    i += 1
    match m:
        case '^':
            dir = (-1, 0)
        case '>':
            dir = (0, 1)
        case '<':
            dir = (0, -1)
        case 'v':
            dir = (1, 0)
    # print(m)
    move(dir)
    # if i > 20:
    #     break

gps = 0
for r in range(1, len(board) - 1):
    for c in range(1, len(board[0]) - 1):
        if board[r][c] == '[':
            gps += c + r*100

print(f"Part 2: {gps}")