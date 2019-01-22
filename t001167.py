import math
num = 100005
flag = [0 for i in range(num)]
rec = [0 for i in range(num)]
cnt = 0
s = 0
flag[0] = 1
for i in range(2, num // 2):
    if not flag[i] and i <= math.sqrt(num):
        for j in range(i * i, num, i):
            flag[j] = 1
for i in range(num - 4):
    if not flag[i]:
        s += 1
    rec[i] = s
try:
    while 1:
        n = [int(i) for i in input().split()]
        cnt += 1
        print("Case %%%d:%d" % (cnt, rec[n[1]] - rec[n[0] - 1]))
except:
    pass
