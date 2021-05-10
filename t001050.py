t = int(input())
for i in range(t):
    n = [int(k) for k in input().split()]
    b1 = n[0]/n[1]
    b2 = n[2]/n[3]
    if b1 >= b2:
        print("iphone 5S")
    else:
        print("iphone 5C")
