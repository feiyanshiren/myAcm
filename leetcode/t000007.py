class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1 if x >= 0 else -1
        e = int(str(abs(x))[::-1]) * f
        return 0 if e > 2147483647 or e < -2147483648 else e


s = Solution()
print(s.reverse(-120))
