import re
for t in range(int(input())):
    s = input()
    b = re.search(r"\+|-", s)
    a = "0x" + s[:b.regs[0][0] + 1] + "0x" +s[b.regs[0][1]:]
    print(oct(eval(a))[2:])
