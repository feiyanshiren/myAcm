def iToR(n):
    c = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
         ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
         ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
         ["","M","MM","MMM"]]
    s = ""
    s += c[3][n // 1000 % 10]
    s += c[2][n // 100 % 10]
    s += c[1][n // 10 % 10]
    s += c[0][n % 10]
    return s

try:
    while 1:
        n = int(input())
        print(iToR(n))
except:
    pass
