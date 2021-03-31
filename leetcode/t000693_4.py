class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0 :
            if n % 2 == (n // 2) % 2:
                return False
            n //= 2
        return True




"""
我们可以通过 n%2 和 n//2 操作获得最后一位和其余的位。如果最后一位等于剩余的最后一位，那么两个相邻的位具有相同的值，则答案是 False 的，反之，答案是 True 的

"""
s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(9223372036854775807))