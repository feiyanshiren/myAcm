def f(n,x):
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x
        y=n%x
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    s = ""
    for i in b:
        s += a[i]
    return s

def intf(sn, x):
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    h = 0
    ll = len(sn)
    for j in range(ll):
        s1 = sn[j]
        for i in range(x):
            b = a[i]
            if s1 == b:
                s1 = i
                break
        d = int(s1) * x ** (ll - j - 1)
        h += d
    return h


for i in range(100, 999):
    s1 = str(i)
    h1 = sum([int(j) for j in s1])
    s2 = hex(i).replace("0x", "")
    h2 = sum([int(j, 16) for j in s2])
    s3 = f(i, 12)
    h3 = sum([intf(j, 12) for j in s3])
    if h1 == h2 and h1 == h3:
        print(i)
