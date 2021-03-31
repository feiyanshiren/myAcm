# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.cc1(root.left)-self.cc1(root.right)) > 1:
            return False
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
            
        
    def cc1(self,tree):
        if tree is None:
            return 0
        else:
            return max(self.cc1(tree.left),self.cc1(tree.right))+1

