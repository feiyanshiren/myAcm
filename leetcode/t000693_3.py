class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = n^(n>>1)
        return tmp&(tmp+1) == 0


"""
将n右移一位异或n，检查结果是否全为1。
"""
s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(9223372036854775807))