# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum:
            if not root.left and not root.right:
                return True
        sum -= root.val
        l = self.hasPathSum(root.left, sum)
        r = self.hasPathSum(root.right, sum)
        return l or r