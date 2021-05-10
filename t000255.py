for t in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().split()]
    m = list({v: 0 for v in s}.keys())
    m.sort()
    print(len(m))
    for i in m: print(i, end=" ")
    print()
