class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""
        p = strs[0]
        for i in range(1, n):
            while not strs[i].startswith(p):
                p = p[0: len(p) - 1]
                if p == "":
                    return ""
        return p

  
        
s = Solution()
print(s.longestCommonPrefix(["flow","flow","flow"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))