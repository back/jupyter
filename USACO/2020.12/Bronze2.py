"""
ID: royone
LANG: PYTHON3
"""

n = int(input())
p = list(map(int, input().split()))

count = n

for i in range(n-1):
    total = p[i]
    items = 1
    for j in range(i+1, n):
        total += p[j]
        items += 1
        if total % items == 0:
            if int(total // items) in p[i:j+1]:
                count += 1

print(count)
