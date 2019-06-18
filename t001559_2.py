for T in range(int(input())):
    s = input().rstrip()
    a = 0
    for i in s:
        if i.isdecimal():
            a += 1
    if a < 4:
        print("No")
    else:
        print("Yes")
