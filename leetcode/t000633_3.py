import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = int(math.sqrt(c))
        for i in range(2, d + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3






s = Solution()

print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(0))
print(s.judgeSquareSum(1))
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(32767))
print(s.judgeSquareSum(2147483647))

