class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = s.lower()
        s2 = list(filter(lambda x: x.isalnum(), s1))
        if s2 == s2[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
