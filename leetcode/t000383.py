class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        for i in magazine:
            m[i] = m.get(i, 0) + 1
        for i in ransomNote:
            v = m.get(i, 0)
            if v <= 0:
                return False
            m[i] = m.get(i, 0) - 1
        return True
    
s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("", ""))