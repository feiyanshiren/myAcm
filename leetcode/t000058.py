class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = s.split()
        a = len(d)
        if a == 0:
            return 0
        else:
            return len(d[-1])
        


s = Solution()
print(s.lengthOfLastWord("a "))