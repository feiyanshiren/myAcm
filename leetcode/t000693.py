class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True

s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(9223372036854775807))