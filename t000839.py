for i in range(int(input())):
    input()
    n1 = [int(n) for n in input().split()]
    n2 = [int(n) for n in input().split()]
    n1 = n1 + n2
    f = {}
    for n in n1:
        f[n] = 0
    n2 = list(f.keys())
    n2.sort()
    t = ""
    for ll in n2:
        t = t + str(ll) + " "
    print(t.strip())
