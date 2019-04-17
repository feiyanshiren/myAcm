class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        b = len(s) // 2
        y = len(s) % 2
        if y != 0:
            a = s[:b]
            c = s[b + 1:]
            c = c[::-1]
            return True if a == c else False
        else:
            a = s[:b]
            c = s[b:]
            c = c[::-1]
            return True if a == c else False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
 