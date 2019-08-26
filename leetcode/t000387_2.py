class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        mm = l
        m = "abcdefghijklmnopqrstuvwxyz"
        for i in m:
            a = s.find(i)
            b = s.rfind(i)
            if a != -1 and a == b:
                mm = min(mm, a)
        return mm if mm != l else -1
    
s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))