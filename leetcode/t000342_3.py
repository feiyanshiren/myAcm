class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and (num & num - 1)==0 and (num & 0x55555555)==num

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(0))
print(s.isPowerOfFour(5))