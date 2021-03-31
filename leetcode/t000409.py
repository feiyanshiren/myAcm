from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = Counter(s)
        c = 0
        b = 1
        for k, v in a.items():
            if v % 2 == 0:
                c += v
            else:
                c += v - 1
                if b:
                    c += 1
                    b = 0
        return c
    
s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("ljsdfioolkdsjfio"))

