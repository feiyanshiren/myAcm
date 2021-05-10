z = [1]
for i in range(2, 21):
    b = 1
    for j in range(1, i + 1, 2):
        b = b * j
    z.append(b + z[-1])

a = int(input())
for i in range(a):
    n = int(input())
    if n == 0:
        print(0)
        continue
    print(z[n - 1])
