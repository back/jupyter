fileName="""
LANG: PYTHON2
TASK: stamps
""".split()[-1]

from time import time
start = time()

with open(fileName + '.in') as fin:
    k, n = map(int, fin.readline().split())
    stamps = [int(i) for line in fin.readlines() for i in line.split()]

p = [k+1] * (k*max(stamps)+2)
p[0] = 0

for v in stamps:
    for i in range(v, v*k+1):
        x = p[i-v] + 1
        if x < p[i]:
            p[i] = x

print('%s' % (time() - start))
answer = p.index(k+1) - 1
print (answer)

with open(fileName + '.out', 'w') as fout:
    fout.write('%s\n' % answer)

print('%s' % (time() - start))
