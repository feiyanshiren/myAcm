class Solution:
    def isHappy(self, n):
        l = {4: 1, 16: 1, 37: 1, 58: 1, 89: 1, 145: 1, 42: 1, 20: 1}
        while n != 1:
            if l.get(n, 0) == 1:
                return False
            l[n] = 1
            n = sum([int(i) ** 2 for i in str(n)])
        return True
        

s = Solution()
print(s.isHappy(19))
print(s.isHappy(20))
print(s.isHappy(21))
print(s.isHappy(28))
print(s.isHappy(18))

