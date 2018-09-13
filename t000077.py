nk = [int(i) for i in input().split()]
m = {}
for i in range(1, nk[0] + 1):
    m[i] = False
for i in range(1, nk[1] + 1):
    for j in m.keys():
        if j % i == 0:
            m[j] = not m[j]
for i in m.keys():
    if m[i]:
        print(i, end=" ")
print()
