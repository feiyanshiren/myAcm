while 1:
    n = [int(i) for i in input().split()]
    if n[0] == 0: break
    n = n[1:]
    w = n.index(min(n))
    n[0], n[w] = n[w], n[0]
    for i in n: print(i, end=" ")
    print()
