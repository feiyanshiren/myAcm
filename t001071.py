try:
    while 1:
        s = input()
        b = [int(i) for i in s.split()]
        if b[0] *  b[1]:
            a = s.count("-")
            if a % 2:
                print("Signs are opposite")
            else:
                print("Signs are not opposot")
        else:
            print("Signs can't be sure")
except: pass