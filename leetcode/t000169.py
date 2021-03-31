class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums) // 2
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        for i in m.keys():
            if m[i] > n:
                return i
    

s = Solution()
print(s.majorityElement([1, 2, 3, 3, 3]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))