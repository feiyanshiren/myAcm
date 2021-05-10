from itertools import permutations
for T in range(int(input())):
    s = input()
    a = []
    if s == "":
        while 1:
            s = input()
            if s == "": break
            a.append(s)
    else:
        while 1:
            a.append(s)
            s = input()
            if s == "": break
    if len(a):
        d = ["".join(i) for i in list(permutations(a))]
        d.sort(reverse=True)
        print(d[0])
        print(d[-1])
            
    
    