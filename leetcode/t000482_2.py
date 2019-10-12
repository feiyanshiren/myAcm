class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s1 = S.upper().replace('-','')
        res = ""
        for i in range(len(s1), 0, -K):
            c = i - K
            if c > 0:
                res = "-" + s1[c: i] + res
            else:
                res = s1[:i] + res
        return res
    

s = Solution()
# print(s.licenseKeyFormatting("a", 2))
# print(s.licenseKeyFormatting("-", 1))
# print(s.licenseKeyFormatting("b", 1))
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
print(s.licenseKeyFormatting("2-4A0r7-4k", 4))