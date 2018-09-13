m={"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12}
try:
    c = 0
    while 1:
        s = input()
        c += 1
        print("Case %d: %d"%(c,m[s]))
except: pass