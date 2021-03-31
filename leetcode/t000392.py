class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            b = t.find(i)
            if b == -1:
                return False
            t = t[b + 1:]
        return True 
            
    
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))