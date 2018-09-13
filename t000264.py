def ifo(s, a):
    ss = a
    l = len(s)
    # k = a[::-1]
    while len(ss) < l:
        ss = ss + ss[::-1]
        # k = k[::-1]
    if ss == s:
        return True
    return False



for n in range(int(input())):
    s = input()
    le = len(s)
    if le == 0:
        print(1)
    elif le == 1:
        print(1)
    elif le % 2 != 0:
        print(le)
    else:
        for i in range(1, le + 1):
            if ifo(s, s[:i]):
                print(i)
                break
