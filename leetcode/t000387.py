class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in range(len(s)):
            ii = s[i]
            if m.get(ii, 0) <= 1:
                return i
        return -1
    
s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
