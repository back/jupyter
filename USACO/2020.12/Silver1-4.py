from sys import stdin

n = int(stdin.readline().split()[0])
data = [ [] for _ in range(n+1) ]

for i in range(n-1):
    a,b = map(int, stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

cost = 0
process = [1]
processed = []

k_cache=[0] * 100
thr = 1
inc = 0
for i in range(100):
    if i>=thr:
        thr *=2
        inc += 1
    k_cache[i] = i+inc

while process:
    i = process.pop(0)
    children = [x for x in data[i] if x not in processed]
    processed.append(i)

    if children:
        process.extend(children)
        k = len(children)
        if k < len(k_cache):
            cost += k_cache[len(children)]
        else:
            cost += k
            while(k):
                k //= 2
                cost += 1
print(cost)
