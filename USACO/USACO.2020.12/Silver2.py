n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

res = set()
for x,y in data:
    newset = set()
    newset.add((x,y,x,y))
    for e in res:
        minx = x if x < e[0] else e[0]
        miny = y if y < e[1] else e[1]
        maxx = x if x > e[2] else e[2]
        maxy = y if y > e[3] else e[3]
        newset.add((minx,miny,maxx,maxy))
    res.update(newset)
    
print(len(res)+1)
