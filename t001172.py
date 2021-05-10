a = [1, 7]
k = 0
while a[-1] <= 1e18:
    a.append(a[k] * 10 + 1)
    a.append(a[k] * 10 + 7)
    k = k + 1
ll = len(a)
try:
    while 1:
        cnt = 0
        n = [int(i) for i in input().split()]
        for i in range(ll):
            if a[i] >= n[0] and a[i] <= n[1]:
                cnt = cnt + 1
        print(cnt)
except EOFError:
    pass
