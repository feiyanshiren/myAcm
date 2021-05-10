a = []
f1 = 1
f2 = 1
a.append(f1)
a.append(f2)
for n in range(2, 50):
    f1 = f1 + f2
    a.append(f1)
    f2 = f1 + f2
    a.append(f2)
while 1:
    x = int(input())
    if x == 0:
        break
    if x in a:
        print("YES")
    else:
        print("NO")
