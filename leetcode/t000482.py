class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s1 = "".join(S.split("-")).upper()[::-1]
        l1 = len(s1)
        res = ""
        for i in range(0, l1, K):
            if i + K < l1:
                res += s1[i: i + K] + "-"
            else:
                res += s1[i:]
        return res[::-1]
    

s = Solution()
print(s.licenseKeyFormatting("a", 2))
print(s.licenseKeyFormatting("-", 1))
print(s.licenseKeyFormatting("b", 1))
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
print(s.licenseKeyFormatting("2-4A0r7-4k", 4))