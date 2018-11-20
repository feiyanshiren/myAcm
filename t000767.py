for t in range(int(input())):
    n = int(input())
    s = 0
    i = 1
    while i * i < n:
        if n % i == 0: s += i + int(n / i)
        i += 1
    if i * i == n: s += i
    if s > n + 1: print("No %d" % s)
    else: print("Yes")