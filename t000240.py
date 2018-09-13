tm = [int(i) for i in input().split()]
d = {}
for t in range(1, tm[0] + 1):
    n = [int(i) for i in input().split()[1:]]
    f = {str(t) + " " + str(k + 1): v for k, v in enumerate(n)}
    d.update(f)
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
dd = {}
for i in range(len(d)):
    if len(dd.get(d[i][1], [])) == 0:
        dd[d[i][1]] = [d[i][0]]
    else:
        dd[d[i][1]].append(d[i][0]) 
h = list(dd.values())
for m in range(tm[1]):
    g = h[int(input()) - 1]
    for i in g: print(i)
