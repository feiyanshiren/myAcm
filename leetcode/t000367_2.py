class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
"""
利用 1+3+5+7+9+…+(2n-1)=n^2，即完全平方数肯定是前n个连续奇数的和
for i in range(1000):
    print("%d, %d" % (i, i * i))
"""
print(s.isPerfectSquare(9223372036854775807))
print(s.isPerfectSquare(9999999800000001))