class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num / r) // 2
        if r * r == num:
            return True
        return False

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
"""
牛顿迭代法
for i in range(1000):
    print("%d, %d" % (i, i * i))
"""
print(s.isPerfectSquare(9223372036854775807))
print(s.isPerfectSquare(9999999800000001))
print(s.isPerfectSquare(99980001))