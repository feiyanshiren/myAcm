from functools import cmp_to_key

class Hy:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        

def _cmp(a, b):
    if a.e == b.e:
        return a.s > b.s
    else:
        return a.e < b.e

for M in range(int(input())):
    m = []
    n = int(input())
    for i in range(n):
        b = [int(j) for j in input().split()]
        hy = Hy(b[0], b[1])
        m.append(hy)
    m.sort(key=cmp_to_key(_cmp))
    tt = m[0].e
    a = 1
    for i in range(1, n):
        if m[i].s >= tt:
            a += 1
            tt = m[i].e
    print(a)
        