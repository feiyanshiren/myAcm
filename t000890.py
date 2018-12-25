for i in range(int(input())):
    m = [int(j) for j in input().split()]
    print("Yes") if m[0] < 2 ** m[1] else print("No")