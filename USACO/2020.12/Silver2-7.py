n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
data.sort()

comb = 1 + n

for i in range(n-1):
    for j in range(i+1,n):
        y0,y1 = (data[i][1],data[j][1]) if data[i][1]<data[j][1] else (data[j][1],data[i][1])
        upper = sum(1 for cow in data[i+1:j] if cow[1]>y1)+1
        lower = sum(1 for cow in data[i+1:j] if cow[1]<y0)+1
        comb += upper * lower

print(comb)
