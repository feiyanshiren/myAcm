for t in range(int(input())):
    a = input().split()
    m = int(a[0])
    k = int(a[1])
    n = int(a[2])
    r = 0
    for i in range(n):
        b = input()
        if (b.startswith(a[3]) or b.endswith(a[3])) and m > 0:
            r += 1
            m -= k
    print(r if r != 0 else "NICE DAY!")
             