for t in range(int(input())):
    n = int(input())
    c = n - int(n / 5) - int(n / 6) - int(n / 8) + int(n / 30) + int(n / 24) + int(n / 40) - int(n / 120)
    print(c)