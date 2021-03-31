class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        m1 = s[0]
        for i in s:
            if i > m1:
                m1 = i
        if len(s) < 3:
            return m1
        m2 = s[0]
        for i in s:
            if i > m2 and i != m1:
                m2 = i
        m3 = s[0]
        for i in s:
            if i > m3 and i != m1 and i != m2:
                m3 = i
        return m3
        
        
    
s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))