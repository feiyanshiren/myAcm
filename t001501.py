a = [["0", " ", "'", '"', "!"],
     ["1", ",", ".", "\\", "?"],
     ["2", "a", "b", "c", "A", "B", "C"], 
     ["3", "d", "e", "f", "D", "E", "F"],
     ["4", "g", "h", "i", "G", "H", "I"],
     ["5", "j", "k", "l", "J", "K", "L"],
     ["6", "m", "n", "o", "M", "N", "O"],
     ["7", "p", "q", "r", "s", "P", "q", "R", "S"],
     ["8", "t", "u", "v", "T", "U", "V"],
     ["9", "w", "x", "y", "z", "W", "X", "Y", "Z"]]
try:
    while 1:
        s = input()
        d = ""
        for i in s:
            for j in range(10):
                aa = a[j]
                if i in aa:
                    d += str(j)
                    break
        print(d)
except:
    pass