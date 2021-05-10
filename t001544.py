for T in range(int(input())):
    n = int(input())
    k = 2 * n - 1
    z = k // 2
    for i in range(k):
        a = abs(z - i)
        b = 2 * (n - a) - 1
        print(" " * a + "*" * b + " " * a)