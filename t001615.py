def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    c = eval(eq1,{var:1j})
    return -c.real/c.imag
try:
    while 1:
        s = input()
        a = ""
        for i in s:
            if i.isalpha():
                a = i
                break
        s1 = ""
        for i in s:
            if i == a:
                if s1 != "" and s1[-1].isalnum():
                    s1 += "*"
            s1 += i
        print("%s=%.3f" % (a, solve(s1, a)))
except:
    pass