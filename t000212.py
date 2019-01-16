for T in range(int(input())):
    n = int(input())
    a = [0 for i in range(1000)]
    b = 0
    if n >= 1000:
        b = 1
        n = n % 1000
    c = 0
    k = 1
    while 1:
        c += 1
        k *= n
        if k >= 1000 or b:
            k = k % 1000
            if a[k] == 0:
                a[k] = c
            else:
                break
    print(c + a[k])
