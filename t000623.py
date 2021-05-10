def mm(A, B):
  return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
while 1:
    mnks = input()
    if mnks == "0 0 0": break
    mnk = [int(i) for i in mnks.split()]
    A = []
    B = []
    for x in range(mnk[0]):
        s = [int(i) for i in input().split()]
        A.append(s)
    for x in range(mnk[1]):
        s = [int(i) for i in input().split()]
        B.append(s)
    C = mm(A, B)
    for i in C:
        for j in i: print("%d " % j, end="")
        print()