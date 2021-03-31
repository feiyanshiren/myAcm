class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in t:
            d = m.get(i, 0)
            if d == 0:
                return i
            else:
                d -= 1
                m[i] = d
        return ""
    
s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("a", "aa"))