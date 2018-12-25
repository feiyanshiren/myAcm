try:
    a = [0 for i in range(100)]
    a[1] = 1
    a[2] = 2
    a[3] = 2
    for i in range(4, 78):
        a[i] = a[i - 3] + a[i - 2]
    while 1:
        print(a[int(input())])
except:
    pass