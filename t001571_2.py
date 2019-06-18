for n in range(int(input())):
    s = input().strip()
    b = ""
    for i in s:
        d = ord(i)
        if d >= 65 and d <= 90:
            b += chr(d + 32)
        else:
            b += i
    print(b)
