import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = int(math.sqrt(c))
        a = [c - i ** 2 for i in range(d + 1)]
        for i in a:
            if int(math.sqrt(i)) ** 2 == i:
                return True
        return False






s = Solution()

print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(0))
print(s.judgeSquareSum(1))
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(32767))
print(s.judgeSquareSum(2147483647))

