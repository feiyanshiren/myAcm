for t in range(int(input())):
    n = [i for i in input().split()]
    m = 0
    for i in n[0]:
        if i == n[1]:
            m += 1
    print(m)
