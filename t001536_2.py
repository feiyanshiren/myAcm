from collections import Counter
try:
    while 1:
        n = [int(i) for i in input().split()]
        a = [[] for i in range(n[1])]
        for i in range(n[0]):
            s = input().split()
            for l in range(len(s)):
                a[l].append(s[l])
            print(Counter(s).most_common()[0][0])
        for i in a:
            print(Counter(i).most_common()[0][0])
except:
    pass