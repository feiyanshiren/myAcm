import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = int(math.sqrt(c))
        for a in range(d + 1):
            b = c - a ** 2
            if self.er_feng(0, b, b):
                return True
        return False

    def er_feng(self, s, e, n):
        if s > e:
            return False
        mid = s + (e - s) // 2
        if mid ** 2 == n:
            return True
        if mid ** 2 > n:
            return self.er_feng(s, mid - 1, n)
        return self.er_feng(mid + 1, e, n)






s = Solution()

print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(0))
print(s.judgeSquareSum(1))
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(32767))
print(s.judgeSquareSum(2147483647))

