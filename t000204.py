def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
s = input()
uc = s.count("U")
sc = s.count("S")
if sc != 0:
    print("Bingo")
else:
    if n == 0:
        print("Fail")
    else:
        an = uc / n
        if 0.497 <= an <= 0.503:
            t = gcd(uc, n)
            print("%d/%d" % (int(uc / t), int(n / t)))
        else:
            print("Fail")

        
