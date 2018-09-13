def se(m, n):
    r = 0
    while m != 0:
        r += m % n
        m = int(m / n)
    return r
while 1:
    n = int(input())
    if n == 0: break
    if se(n, 10) == se(n, 16) == se(n, 12):
        print(str(n) + " is a Sky Number.")
    else:
        print(str(n) + " is not a Sky Number.")