class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = list(str(int("".join([str(i) for i in digits])) + 1))
        d = [int(i) for i in s]
        return d


s = Solution()
print(s.plusOne([1,2,3]))