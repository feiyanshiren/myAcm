for i in range(int(input())):
    s = input().split()
    l1 = sum([int(j) for j in list(s[0])])
    l2 = sum([int(j) for j in list(s[1])])
    print(l1 * l2)
