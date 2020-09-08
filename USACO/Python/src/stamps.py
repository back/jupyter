fileName="""
LANG: PYTHON2
TASK: stamps
""".split()[-1]

fin=open(fileName + '.in')
k, n = map(int, fin.readline().split())
stamps = [int(i) for line in fin.readlines() for i in line.split()]

p = [0] * (k*max(stamps)+2)

for i in range(1, len(p)):
    p[i] = min(p[i-v] for v in stamps if i >= v) + 1
    if p[i] > k:
        break
    
fout = open(fileName + '.out', 'w')
fout.write('%s\n' % (i-1))
fout.close()
