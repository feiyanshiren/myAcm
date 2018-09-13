t = int(input())
for i in range(t):
    ss = input().split()
    ll = len(ss)
    he = 0
    for s in range(1, ll):
        he = he + int(ss[s])
    print(he)
