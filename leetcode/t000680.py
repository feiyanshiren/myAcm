class Solution:
    def validPalindrome(self, s: str) -> bool:
        b = s[::-1]
        if b == s:
            return True
        else:
            l = len(s)
            for i in range(l):
                c = ""
                if i == 0:
                    c = s[1:]
                elif i == l -1:
                    c = s[:-1]
                else:
                    c = s[:i] + s[i + 1:]
                b = c[::-1]
                if b == c:
                    return True
            return False



s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abababababababababababababababababababac"))
