nt = [int(i) for i in input().split()]
g = [-1 for i in range(nt[0])]
f = 0
for i in range(nt[1]):
    s = input().split()
    if len(s) > 1:
        d = int(s[1]) - 1
        g[d] = -g[d]
        if g[d] == 1:
            f += 1
        else:
            f -= 1
    else:
        print(f)
