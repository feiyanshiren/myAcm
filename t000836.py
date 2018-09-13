for i in range(int(input())):
    n = int(input())
    for d in range(n):
        t = ""
        for k in range(n - d):
            t = t + "*"
        print(t)
