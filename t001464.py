for T in range(int(input())):
    N = int(input())
    m = [int(i) for i in input().split()]
    s = 0
    z = 0
    for i in m:
        c = abs(i - s)
        if s <= i:
            z += c * 6 + 5
        else:
            z += c * 4 + 5
        s = i
    print(z)
