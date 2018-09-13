t = int(input())
for i in range(t):
    s = input()
    k = input()
    sl = len(s)
    kl = len(k)
    cnt = 0
    ll = sl - kl + 1
    for j in range(0, ll):
        ss = s[j: j + kl]
        if ss == k:
            cnt += 1
    print(cnt)
