def addt(a, n, b):
    n = n.split()[1]
    a.insert(0, n)

def addw(a, n, b):
    n = n.split()[1]
    a.append(n)
    
def delt(a, n, b):
    try:
        a.pop(0)
    except:
        pass
    
def delw(a, n, b):
    try:
        a.pop()
    except:
        pass
    
def g(a, n, b):
    b["0"], b["1"] = b["1"], b["0"]
    b["2"], b["3"] = b["3"], b["2"]
    
for T in range(int(input())):
    a = []
    b = {"0": addt, "1": addw, "2": delt, "3": delw, "4": g}
    for n in range(int(input())):
        s = input()
        b[s[0]](a, s, b)
    if len(a):
        print(" ".join(a))
    else:
        print(-1)

    