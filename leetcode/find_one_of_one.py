import os

ll = os.listdir("./")
print(ll)

ss = [i.split(".")[0] for i in ll]

print(ss)

aa = [i.split("_")[0] for i in ss]

print(aa)

bb = {}

for i in aa:
    bb[i] = bb.get(i, 0) + 1
    
print(bb)

cc = []

for k, v in bb.items():
    if v == 1:
        cc.append(k)
        
print(cc)