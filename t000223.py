m = {"0": "0", "1": "1"}
m.update({i: "2" for i in "abc"})
m.update({i: "3" for i in "def"})
m.update({i: "4" for i in "ghi"})
m.update({i: "5" for i in "jkl"})
m.update({i: "6" for i in "mno"})
m.update({i: "7" for i in "pqrs"})
m.update({i: "8" for i in "tuv"})
m.update({i: "9" for i in "wxyz"})
for t in range(int(input())):
    print("".join([m[i] for i in input()]))
