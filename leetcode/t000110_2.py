# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):

        def isB(root):
            if not root:return True,0
            lb,ls = isB(root.left)
            rb,rs = isB(root.right)
            return lb and rb and abs(ls - rs) <= 1, max(ls, rs) + 1

        return isB(root)[0]

