n = int(input())
aaa = []
for i in range(n):
    a = input()
    b = ""
    for i in range(len(a) - 1, -1, -1):
        aa = a[i]
        if aa.isdigit() or aa == " ":
            continue
        else:
            b = b + aa
    aaa.append(b)
for i in aaa:
    print(i)
