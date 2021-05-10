for T in range(int(input())):
    m = int(input())
    for j in range(7):
        ab = [int(i) for i in input().split()]
        m -= ab[1] - ab[0]
    if m <= 0:
        print("YES")
    else:
        print("NO")