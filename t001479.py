try:
    while 1:
        n = [int(i) for i in input().split()]
        k = n[0] + 1
        while k % n[1] == 0 or str(n[1]) in str(k):
             k += 1
        print(k)
except:
    pass
