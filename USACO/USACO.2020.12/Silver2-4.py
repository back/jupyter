n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

comb = 1 + n
print('comb=', comb)
for i in range(n-1):
    for j in range(i+1,n):
        minx,maxx = (data[i][0],data[j][0]) if data[i][0]<data[j][0] else (data[j][0],data[i][0])
        miny,maxy = (data[i][1],data[j][1]) if data[i][1]<data[j][1] else (data[j][1],data[i][1])
        comb += 1 + len([x for x in data if x[0]>minx and x[0] < maxx and (x[1]>maxy or x[1]<miny)])

print(comb)
