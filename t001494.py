def ifs(s, p, f):
    i = s.find(p)
    if i != -1:
        k = s.find(f)
        if k < i:
            return True
        else:
            return False
    else:
        return True
    

t_map = {
    "13": "2", "31": "2",
    "19": "5", "91": "5",
    "28": "5", "82": "5",
    "17": "4", "71": "4",
    "37": "5", "73": "5",
    "39": "6", "93": "6",
    "46": "5", "64": "5",
    "79": "8", "97": "8",
}

for T in range(int(input())):
    s = input()
    b = "YES"
    for k, v in t_map.items():
        if not ifs(s, k, v):
            b = "NO"
            break
    print(b)
    

    
        