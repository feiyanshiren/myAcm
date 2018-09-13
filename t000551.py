try:
    while 1:
        c = int(input())
        if c >= 90: print("A")
        elif c >= 80 and c < 90: print("B")
        elif c >= 70 and c < 80: print("C")
        elif c >= 60 and c < 70: print("D")
        else: print("E")
except: pass