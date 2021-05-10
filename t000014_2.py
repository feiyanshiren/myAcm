for m in range(int(input())):
    a = []
    for i in range(int(input())):
        a.append([int(j) for j in input().split()])
    a.sort(key=lambda x: x[1])
    h = 1
    b = a[0][1]
    for i in a:
        if i[0] > b:
            b = i[1]
            h += 1
    print(h)