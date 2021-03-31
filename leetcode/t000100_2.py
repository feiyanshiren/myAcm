# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #先判断是否全为空，是则返回；再判断是否有一个为空，是则返回，再判断两个值是否相等
        if not p and not q:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)