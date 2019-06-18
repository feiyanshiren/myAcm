for t in range(int(input())):
    n = [int(i) for i in input().split()]
    for i in range(n[1]):
        if n[0] % 10 != 0:
            n[0] -= 1
        else:
            n[0] //= 10 
    print(n[0])
        