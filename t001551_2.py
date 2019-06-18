def f(n, m):
    if m == 1:
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
        return n
    else:
        return f(f(n, 1), m - 1)
    
for t in range(int(input())):
    n = [int(i) for i in input().split()]
    print(f(n[0], n[1]))
        