# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.getD(root)
    
    def getD(self, root):
        if root is None:
            return 0
        if root.right is None:
            return self.getD(root.left) + 1
        if root.left is None:
            return self.getD(root.right) + 1
        l = self.getD(root.left) + 1
        r = self.getD(root.right) + 1
        if l < r:
            return l
        else:
            return r
