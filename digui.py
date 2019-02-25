a = [1, 2, 3]

def sum1(a):
    if a is None or len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        return a.pop() + sum1(a)
print(sum1(a))


def ef(a, b):
    lq = len(a)
    if lq == 1:
        if a[0] == b:
            return a[0]
        else:
            return None
    else:
        l1 = []
        f = lq // 2
        if b == a[f]:
            return a[f]
        elif b > a[f]:
            l1 = a[f + 1: -1]
        else:
            l1 = a[0, f]
        return ef(l1, b)


def sq(a):
    lq = len(a)
    if lq == 0 or lq == 1:
        return a
    else:
        l1 = []
        l2 = []
        z = a.pop()
        for i in a:
            if i <= z:
                l1.append(i)
            else:
                l2.append(i)
        return sq(l1) + [z] + sq(l2)

print(sq([1, 2, 3, 4, 1, 4, 6, 8, 4, 2]))
        
print(ef([1, 2, 3, 4, 5], 3))
