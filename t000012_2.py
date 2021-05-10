a = [[1, 4], [2, 4], [2, 6], [3, 5], [3, 6], [3, 7], [6, 8]]
s = [7, 8, 8]
b = []
d = 0
b.append(a.pop(0))
d += b[0][1] - b[0][0]
c = 1
while d < s[1]:
    e = []
    f = a[0]
    while f[0] <= b[-1][1] and f[1] >= b[-1][0]:
        e.append(f)
        a.pop(0)
        if len(a) != 0:
            f = a[0]
        else:
            break
    e.sort(key=lambda x: x[1])
    t = e[-1]
    b.append(t)
    d += t[1] - t[0]
    c += 1
print(c)
print(b)