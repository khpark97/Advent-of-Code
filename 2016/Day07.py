## STARTER CODE
file = open('2016/Day07_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

def tls_scan(text):
    for i in range(len(text) - 3):
        if text[i] == text[i+3] and text[i+1] == text[i+2] and text[i] != text[i+1]:
            return True
    return False

def ssl_scan(texts):
    res = []
    for text in texts:
        for i in range(len(text) - 2):
            if text[i] == text[i+2] and text[i] != text[i+1]:
                res.append(''.join([text[i+1], text[i], text[i+1]]))
    return res

tls, ssl = 0, 0
for l in lines:
    split = l.split('[')
    outside = [split[0]]
    brackets = []
    for s in split[1:]:
        left, right = s.split(']')
        outside.append(right)
        brackets.append(left)
    
    if not any([tls_scan(b) for b in brackets]):
        if any([tls_scan(o) for o in outside]):
            tls += 1

    valid = ssl_scan(outside)
    if any([v in ''.join(brackets) for v in valid]):
        ssl += 1

print(f"Part 1: {tls}")

# PART 2

print(f"Part 2: {ssl}")