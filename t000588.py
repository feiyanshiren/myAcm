for t in range(int(input())):
    n = int(input())
    f = 0
    for x in range(10*n+1):
        for y in range(5*n+1):
            for z in range(2*n+1):
                if x+2*y+5*z == 10*n:
                    f += 1
    print(f)
