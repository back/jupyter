"""
ID: royone
LANG: PYTHON3
"""

inputs = list(map(int, input().split()))

inputs.sort()

a,b = inputs[0],inputs[1]
c = inputs[-1]-a-b
print(a,b,c)
