import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return collections.Counter(magazine) & collections.Counter(ransomNote) == collections.Counter(ransomNote)

s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("", ""))