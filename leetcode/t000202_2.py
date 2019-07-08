class Solution:
    def isHappy(self, n):
        l = [4, 16, 37, 58, 89, 145, 42, 20]
        while n != 1:
            if n in l:
                return False
            l.append(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True
        

s = Solution()
print(s.isHappy(19))
print(s.isHappy(20))
print(s.isHappy(21))
print(s.isHappy(28))
print(s.isHappy(18))

