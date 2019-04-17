def if_e(n, m):
    if n == 1:
        return "Ye1s"
    elif n != 1 and n < m:
        return "No"
    elif m == 1:
        return "No"
    else:
        k = n // m
        y = n % m
        n = k + y
        return if_e(n, m)

for t in range(int(input())):
    n = [int(i) for i in input().split()]
    print(if_e(n[0], n[1]))
    