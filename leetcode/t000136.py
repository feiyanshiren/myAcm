class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = None
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        for k, v in m.items():
            if v == 1:
                r = k
                break
        return r

s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 1, 2, 1, 2]))



