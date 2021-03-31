class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        return ('00' not in s) and ('11' not in s)


s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(9223372036854775807))