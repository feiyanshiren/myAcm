class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = s * 2
        if s in a[1:-1]:
            return True
        return False
    
    
s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))