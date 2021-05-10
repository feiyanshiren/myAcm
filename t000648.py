a = []
for i in range(1, 100001):
    a.append(str(i).count("1"))
try:
    while 1:
        n = int(input())
        if n == 0:
            print(0)
            continue
        print(sum(a[0: (n - 1)]))
except EOFError:
    pass
