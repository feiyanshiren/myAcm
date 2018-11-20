try:
    while 1:
        n = int(input())
        if n % 2 != 0:
            print("NO")
            continue
        s = [int(j) for j in input().split()]
        t = [int(j) for j in input().split()]
        s.sort()
        t.sort()
        z = 0
        for i in range(int(n / 2)):
            if s[i] > t[int(n / 2) + i]: z += 1
        for i in range(int(n / 2)):
            if s[int(n / 2) + i] > t[i]: z += 1
        print("YES") if int(n / 2) == z else print("NO")
except: pass