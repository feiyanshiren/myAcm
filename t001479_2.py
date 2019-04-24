def ff(d, k):
    if k % d != 0 and str(d) not in str(k):
        return k
    else:
        return ff(d, k + 1)
        

try:
    while 1:
        n = [int(i) for i in input().split()]
        print(ff(n[1], n[0] + 1))
except:
    pass
