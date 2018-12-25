class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""
        elif "" in strs:
            return ""
        elif n == 1:
            return strs[0]
        else:
            strs.sort(key=lambda x:len(x))
            a = strs.pop(0)
            k = ""
            for i in a:
                k += i
                for j in strs:
                    if not j.startswith(k):
                        return k[:-1]
            return k
  
        
s = Solution()
print(s.longestCommonPrefix(["flow","flow","flow"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))