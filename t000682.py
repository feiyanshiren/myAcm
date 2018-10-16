for t in range(int(input())):
    m = int(input())
    s = input()
    n = int(input())
    k = n % m
    a = list(s)
    for i in range(k):
        b = a.pop(0)
        a.append(b)
    print("".join(a))

