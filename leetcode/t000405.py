class Solution(object):
    def __init__(self):
        self.m = '0123456789abcdef'
        self.k = {k: v for k, v in enumerate(list(self.m))}

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            q = self.q2(num * -1)
            q = self.qf(q)
        else:
            q = self.q2(num)
        return self.et16(q)
    
    def q2(self, num):
        s = ""
        while num // 2 != 0:
            a = num // 2
            b = num % 2
            s = str(b) + s
            num = a
        if num != 0:
            s = str(num) + s
        return s
    
    def qf(self, s):
        a = ""
        for i in s:
            if i == "0":
                a += "1"
            else:
                a += "0"
        while len(a) < 32:
            a = "1" + a
        a = self.bu(a)
        return a
    
    def bu(self, s):
        a = list(s)
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "0":
                a[i] = "1"
                break
            else:
                a[i] = "0"
        return "".join(a)
                
    def et16(self, s):
        a = list(s)
        l = len(a)
        if l> 4:
            a = s[-4:]
            b = s[:-4]
            return self.et16(b) + self.et16(a)
        elif l == 4:
            b = 0
            if a.pop() == "1":
                b += 1
            else:
                b += 0
            if a.pop() == "1":
                b += 2
            else:
                b += 0
            if a.pop() == "1":
                b += 4
            else:
                b += 0
            if a.pop() == "1":
                b += 8
            else:
                b += 0
            return self.k[b]
        elif l == 3:
            b = 0
            if a.pop() == "1":
                b += 1
            else:
                b += 0
            if a.pop() == "1":
                b += 2
            else:
                b += 0
            if a.pop() == "1":
                b += 4
            else:
                b += 0
            return self.k[b]
        elif l == 2:
            b = 0
            if a.pop() == "1":
                b += 1
            else:
                b += 0
            if a.pop() == "1":
                b += 2
            else:
                b += 0
            return self.k[b]
        elif l == 1:
            b = 0
            if a.pop() == "1":
                b += 1
            else:
                b += 0
            return self.k[b]
    
s = Solution()
print(s.qf(s.q2(2147483647)))
print(s.et16("10000000000000000000000000000001"))
print(s.toHex(123))
print(s.toHex(-88))
print(s.toHex(-543564356))
