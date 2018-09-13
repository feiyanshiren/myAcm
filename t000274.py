n = int(input())
a = []
pi = 3.1415926
for i in range(n):
    aa = float(input())
    aaa = pi * ((aa * aa) / 3)
    aaaa = "%.2f" % aaa
    a.append(aaaa)
for i in a:
    print(i)
