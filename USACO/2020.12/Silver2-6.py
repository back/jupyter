n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
data.sort()

comb = 1 + n

for i in range(n-1):
    for j in range(i+1,n):
        y0,y1 = (data[i][1],data[j][1]) if data[i][1]<data[j][1] else (data[j][1],data[i][1])
        upper = lower = 1
        for k in range(i+1, j):
            if data[k][1]>y1:
                upper += 1
            elif data[k][1]<y0:
                lower += 1
        comb += upper * lower

print(comb)
