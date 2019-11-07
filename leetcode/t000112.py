# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        s = sum - root.val
        if not root.left and not root.right:
            return s == 0
        return self.hasPathSum(root.left, s) or self.hasPathSum(root.right, s)