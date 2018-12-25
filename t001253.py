while 1:
    s = input()
    if s == "0+0=0":
        break
    a = s.split("=")
    b = a[0].split("+")
    if int(b[0][::-1]) + int(b[1][::-1]) == int(a[1][::-1]):
        print("TRUE")
    else:
        print("FALSE")
    