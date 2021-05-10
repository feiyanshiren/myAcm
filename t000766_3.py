def is_huiwen(num):
    s = str(num)
    return s == s[::-1]


def is_all_huiwen(n):
    return is_huiwen(n) and is_huiwen(n*n) and is_huiwen(n*n*n)


ll = [x for x in range(1, 1000001) if is_all_huiwen(x)]
for i in range(len(ll)):
    if i == len(ll) - 1:
        print(ll[i])
    elif i % 5 == 4:
        print(ll[i])
    else:
        print(ll[i], end=' ')
