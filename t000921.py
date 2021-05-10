a = [0, 1]
s = 1
for i in range(2, 50000):
    s += 2 * 1.0 / i
    a.append(a[i - 1] + s)
while 1:
    n = int(input())
    if n == 0: break
    print("%.2lf" % a[n])
