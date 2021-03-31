class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and 1073741824 % num == 0

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(0))
print(s.isPowerOfFour(5))