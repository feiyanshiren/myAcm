n = int(input())
a = []
for i in range(n):
    aa = input()
    count = 0
    for aaa in aa:
        if aaa.islower():
            count = count + 1
    yu = count % 26
    if yu == 0:
        a.append("z")
    else:
        a.append(chr(yu + 96))
for i in a:
    print(i)
