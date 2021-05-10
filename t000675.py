try:
    while 1:
        z = {"rat": [], "woman": [], "man": [], "captain": []}
        for i in range(int(input())):
            s = input().split()
            if s[1] == "child": z["woman"].append(s[0])
            else: z[s[1]].append(s[0])
        d = []
        d.extend(z["rat"])
        d.extend(z["woman"])
        d.extend(z["man"])
        d.extend(z["captain"])
        for i in d: print(i)
except: pass