n = int(input())
data=[[0]*(n+1) for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    data[a][b] = data[b][a] = 1

cost = 0
process = [1]
processed = []
while process:
    i = process.pop(0)
    children = [index for index, value in enumerate(data[i]) if value and value not in processed]
    processed.append(i)

    if children:
        #print(children)
        kids = len(children)
        cost += kids
        while(kids):
            kids //= 2
            cost += 1

print(cost)
