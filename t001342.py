a = [1, 2]
for i in range(2, 31):
    a.append(a[i - 1] + a[i - 2])
try:
    while 1:
        d = int(input())
        if d > 30:
            print(a[29])
        else:
            print(a[d - 1])
except:
    pass