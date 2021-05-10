for N in range(int(input())):
    s = [i for i in input().split("=")]
    try:
        d = int(eval(s[0]))
        if d == int(s[1]): print("Accept")
        else:
            print("Wrong Answer")
            print(d)
    except: print("Input Error")