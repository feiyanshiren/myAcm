n = int(input())
f = []
for i in range(n):
    t = 1
    m = int(input())
    for mm in range(m):
        t = 2 * t + 2
    f.append(t)
for i in f:
    print(i)
