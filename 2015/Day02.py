## STARTER CODE
file = open('2015/Day02_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1

paper = 0
ribbon = 0
for l in lines:
    l, w, h = [int(m) for m in l.split('x')]
    paper += 2*l*w + 2*w*h + 2*l*h + min(l*w, w*h, l*h)

    ribbon += l*w*h + sum((sorted([l, w, h])[:2]) * 2)

print(f"Part 1: {paper}")

# PART 2

print(f"Part 2: {ribbon}")