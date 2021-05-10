def f(x, n):
    if n == 1:
        return x
    else:
        return f(x, n - 1) + int(str(x) * n)

try:
    while 1:
        s = [int(i) for i in input().split()]
        print(f(s[0], s[1]))
except:
    pass
