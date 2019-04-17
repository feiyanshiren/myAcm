for T in range(int(input())):
    a = [int(i) for i in input().split()]
    b = a[0] ** a[1]
    k = b % 19260817 
    print(k)
