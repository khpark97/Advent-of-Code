## STARTER CODE
file = open('2022/Day12_data.txt', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
import heapq

s, e = (), ()
a = []
for r in range(len(lines)):
    for c in range(len(lines[0])):
        tile = lines[r][c]
        if tile == 'S':
            s = (r, c)
            a.append((r, c))
            lines[r] = lines[r][:c] + 'a' + lines[r][c+1:]
        elif tile == 'E':
            e = (r, c)
            lines[r] = lines[r][:c] + 'z' + lines[r][c+1:]
        elif tile == 'a':
            a.append((r, c))

def bfs(start):
    q = [(1, start)]
    seen = set([start])
    while q:
        score, (r, c) = heapq.heappop(q)
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = tuple(map(sum, zip((r, c), d)))
            if (nr, nc) not in seen and nr in range(len(lines)) and nc in range(len(lines[0])):
                if ord(lines[nr][nc]) <= 1 + ord(lines[r][c]):
                    if (nr, nc) == e:
                        q = []
                        return score
                    seen.add((nr, nc))
                    heapq.heappush(q, (score + 1, (nr, nc)))
    return float('inf')

print(f"Part 1: {bfs(s)}")

# PART 2

low = float('inf')
for start in a:
    low = min(low, bfs(start))

print(f"Part 2: {low}")