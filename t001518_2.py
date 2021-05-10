try:
    while 1:
        s = [int(i) for i in input().split()]
        t = s[0] / s[2]
        h = t * (s[3] - 5 * t)
        print("Win!") if h > s[1] else print("Lose!")
except:
    pass
