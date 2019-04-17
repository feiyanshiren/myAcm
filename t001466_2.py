for t in range(int(input())):
    n = [int(i) for i in input().split()]
    if n[1] == 1:
        print("No")
        continue
    while n[0] >= n[1]:
        c = n[0] // n[1]
        b = n[0] % n[1]
        n[0] = c + b
    if n[0] == 1:
        print("Yes")
    else:
        print("No")
    