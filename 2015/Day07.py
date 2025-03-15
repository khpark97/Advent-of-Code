## STARTER CODE
file = open('2015/Day07_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

from collections import deque

def run(part):
    vars = {} if part == 'a' else {'b': part}
    q = deque(lines)

    while q:
        curr = q.popleft()
        split = curr.split()
        var2, res = split[-3], split[-1]
        if res == 'b' and part != 'a':
            continue
        
        if len(split) == 3:
            if str.isdigit(var2):
                vars[res] = int(var2)
            else:
                if var2 not in vars:
                    q.append(curr)
                    continue
                vars[res] = vars[var2]

        elif len(split) == 4:
            if str.isdigit(var2):
                vars[res] = ~int(var2)
            else:
                if var2 not in vars:
                    q.append(curr)
                    continue
                vars[res] = ~vars[var2]

        else:
            var1, command = split[0], split[1]

            if ((not str.isdigit(var1) and var1 not in vars) or
                (not str.isdigit(var2) and var2 not in vars)):
                q.append(curr)
                continue
            
            var1 = int(var1) if str.isdigit(var1) else vars[var1]
            var2 = int(var2) if str.isdigit(var2) else vars[var2]

            match command:
                case 'AND':
                    vars[res] = var1 & var2
                case 'OR':
                    vars[res] = var1 | var2
                case 'LSHIFT':
                    vars[res] = var1 << var2
                case 'RSHIFT':
                    vars[res] = var1 >> var2
    return vars

print(f"Part 1: {run('a')['a']}")

# PART 2

print(f"Part 2: {run(run('a')['a'])['a']}")