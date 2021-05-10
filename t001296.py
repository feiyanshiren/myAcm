while 1:
    n = [int(i) for i in input().split()]
    if len(n) == 1 and n[0] == 0:
        break
    if n[0] == 0 or n[1] == 0 or n[2] == 0:
        print("oh,my god!", end="\n")
    else:
        if n[0] + n[1] > n[2] and\
           n[0] + n[2] > n[1] and\
           n[1] + n[2] > n[0]:
            print("Great,you are genius!", end="\n")
        else:
            print("oh,my god!", end="\n")
