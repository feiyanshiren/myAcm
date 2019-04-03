class Solution:
    def titleToNumber(self, s: str) -> int:
        a = 0
        ll = len(s)
        for i in range(ll):
            k = ll - i - 1
            a += (ord(s[i]) - 64) * (26 ** k)
        return a

s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("B"))
print(s.titleToNumber("C"))
print(s.titleToNumber("Z"))
print(s.titleToNumber("AA"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
