while True:
    n = int(input())
    if n == 0:
        break
    ss = sum([int(s) * int(s) for s in input().split()])
    print(ss)
