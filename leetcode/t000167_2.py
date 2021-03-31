class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1      
        while left < right:
            if numbers[left] + numbers[right] == target:                
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                right = right - 1

s = Solution()
print(s.twoSum([3, 3], 6))
