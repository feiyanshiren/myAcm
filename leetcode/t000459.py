class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = ""
        l1 = len(s)
        for i in s:
            a += i
            l2 = len(a)
            k = l1 // l2
            if k <= 1:
                return False
            b = a * k
            if b == s:
                return True
        return False
    
    
s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))