m = {6: "6=1+2+3", 28: "28=1+2+4+7+14",
496: "496=1+2+4+8+16+31+62+124+248",
8128: "8128=1+2+4+8+16+32+64+127+254+508+1016+2032+4064"}
while 1:
    n = int(input())
    if n == -1: break
    if n in m.keys(): print(m[n])
    else: print("No")
        
