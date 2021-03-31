class Solution:
    def dd(self, s, e, n):
        if s == e:
            return s, e
        if e - s == 1:
            return s, e
        d = (e - s) // 2 + s
        c = d * d
        if c == n:
            return d, d
        else:
            if c > n:
                e = d
                return self.dd(s, e, n)
            else:
                s = d
                return self.dd(s, e, n)
    
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        else:
            s = 0
            e = num
            d = num // 2
            c = d * d
            if c == num:
                return True
            else:
                s, e = self.dd(s, e, num)
                for i in range(s, e + 1):
                    if i * i == num:
                        return True
            return False

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
"""
for i in range(1000):
    print("%d, %d" % (i, i * i))
"""
print(s.isPerfectSquare(9223372036854775807))
print(s.isPerfectSquare(9999999800000001))