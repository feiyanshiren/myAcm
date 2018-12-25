for n in range(int(input())):
    m = [int(i) for i in input().split()]
    a = []
    while m[0]:
        a.insert(0, str(m[0] % m[1]))
        m[0] = int(m[0] / m[1])
    print("".join(a))