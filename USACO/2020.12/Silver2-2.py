"""
ID: royone
LANG: PYTHON3
"""

n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
data.sort()

dp = [1] * n

for i in range(1,n):
    x,y = data[i]
    for j in range(i):
        _, jy = data[j]
        blocked = False
        for _, ky in data[j+1:i]:
            if (jy < ky) == (ky < y):
                blocked = True
                break
        if not blocked:
            dp[i] += dp[j]

print(dp)
print(sum(dp)+1)
