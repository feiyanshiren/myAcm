for t in range(int(input())):
    b = [int(i) for i in input().split()[1:]]
    b.sort()
    print(b[-1] - b[0])
