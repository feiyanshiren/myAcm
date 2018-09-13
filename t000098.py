p = {"9": "A", "8": "B", "7": "C", "6": "D",
     "5": "E", "4": "E", "3": "E", "2": "E", "1": "E",
     "0": "E"}
for i in range(int(input())):
    m = input()
    print(p["9" if m == "100" else m[0]])
