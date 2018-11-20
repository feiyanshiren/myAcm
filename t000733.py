def ifz(s):
    if "9" in s or "8" in s or "7" in s: return False
    else:
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]: return False
        for i in range(len(s) - 1):
            if abs(int(s[i]) - int(s[i + 1])) > 4: return False
        return True
for n in range(int(input())):
    s = input().split()
    for i in range(int(s[0]), int(s[1]) + 1):
        k = str(i)
        while len(k) < 6: k = "0" + k
        if ifz(str(k)): print(k)
