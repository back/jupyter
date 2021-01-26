"""
ID: royone
LANG: PYTHON3
"""
import math

n = int(input())
data=[]

for i in range(n-1):
    a,b = map(int, input().split())
    data.append((a,b))

cost = 0
process = [1]
while process:
    i = process.pop(0)
    newData = []
    children = 0
    for a, b in data:
        if a==i:
            process.append(b)
            children += 1
        elif b==i:
            process.append(a)
            children += 1
        else:
            newData.append((a,b))
    if children:
        cost += children
        cost += math.ceil(math.log(children+1, 2))
    data = newData       

print(cost)
