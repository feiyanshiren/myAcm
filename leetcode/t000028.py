class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

s = Solution()
print(s.strStr("aaaaa", "bba"))
print(s.strStr("aaaaa", ""))