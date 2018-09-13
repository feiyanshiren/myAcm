n = int(input())
for i in range(n):
    s = [float(k) for k in input().split()]
    s.sort()
    p = (s[0] + s[3] + s[6]) / 3
    print("%.2f" % p)
