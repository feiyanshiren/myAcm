import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
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

