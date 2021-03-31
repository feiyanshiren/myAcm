# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        return self.b(nums, 0, len(nums) - 1)
        
    def b(self, nums, l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        root = TreeNode(nums[m])
        root.left = self.b(nums, l, m - 1)
        root.right = self.b(nums, m + 1, r)
        return root


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))