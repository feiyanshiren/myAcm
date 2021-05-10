a = [i * i for i in range(32000)]
try:
    while 1:
        n = int(input())
        if n in a:
            print("YES")
        else:
            print("NO")
except:
    pass