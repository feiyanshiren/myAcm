try:
    while 1:
        s = [int(i) for i in input().split()]
        tx = s[0] / s[2]
        hy = (s[3] * tx) - (0.5 * 10 * tx ** 2)
        if hy > s[1]:
            print("Win!")
        else:
            print("Lose!")
except:
    pass
