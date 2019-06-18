try:
    while 1:
        s = input()
        k = 0
        n = len(s)
        for i in range(n - 1):
            k = i
            if s[i] <= s[i + 1]:
                print(s[i], end="")
            else:
                break
        for i in range(k + 1, n):
            print(s[i], end="")
        print()
except:
    pass