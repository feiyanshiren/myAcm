n = int(input())
for i in range(n):
    p = [int(j) for j in input().split()]
    s = int(input()) + 30
    n = 0
    for j in p:
        if j <= s:
            n = n + 1
    print(n)
