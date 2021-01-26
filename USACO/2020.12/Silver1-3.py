from sys import stdin

n = int(stdin.readline().split()[0])
data = [ [] for _ in range(n+1) ]

for i in range(n-1):
    a,b = map(int, stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

print(data)

cost = 0
process = [1]
processed = []

while process:
    i = process.pop(0)
    children = [x for x in data[i] if x not in processed]
    processed.append(i)

    if children:
        process.extend(children)
        kids = len(children)
        cost += kids
        while(kids):
            kids //= 2
            cost += 1

print(cost)
