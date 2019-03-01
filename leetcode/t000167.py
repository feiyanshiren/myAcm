class Solution:
    def twoSum(self, numbers, target):
        m = {j: i for i, j in enumerate(numbers)}
        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in m and m[a] != i:
                return [i + 1, m[a] + 1]

s = Solution()
print(s.twoSum([3, 3], 6))
