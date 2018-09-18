def h(x, y):
    s = x
    if x > y: s = y
    r = 1
    for i in range(1,s + 1):
        if((x % i == 0) and (y % i == 0)): r = i
    return r
try:
    while 1:
        d = [int(i) for i in input().split(",")]
        print(h(d[0], d[1]))
except: pass