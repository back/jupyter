n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

comb = 1 + n

for i in range(n-1):
    for j in range(i+1,n):
        minx,maxx = (data[i][0],data[j][0]) if data[i][0]<data[j][0] else (data[j][0],data[i][0])
        miny,maxy = (data[i][1],data[j][1]) if data[i][1]<data[j][1] else (data[j][1],data[i][1])
        upper = lower = 1
        for cow in data:
            if cow[0]>minx and cow[0]<maxx:
                if cow[1]>maxy:
                    upper += 1
                elif cow[1]<miny:
                    lower += 1
        comb += upper * lower

print(comb)
