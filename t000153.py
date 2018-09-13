for i in range(int(input())):
    n = int(input())
    x = [int(j) for j in input().split()]
    y = [int(j) for j in input().split()]
    x.sort()
    y.sort()
    xf = 0
    yf = 0
    for j in range(n):
        if x[j] > y[j]:
            xf = xf + 2
        elif x[j] == y[j]:
            xf = xf + 1
            yf = yf + 1
        else:
            yf = yf + 2
    print("X") if xf > yf else print("none") if xf == yf else print("Y")
