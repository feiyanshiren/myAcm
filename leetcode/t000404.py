# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.summ(0, root)
    
    
    def summ(self, n, root):
        if not root:
            return n
        if not root.left and not root.right:
            return n
        elif root.left and not root.right:
            if not root.left.left and not root.left.right:
                return n + root.left.val
            else:
                return self.summ(n, root.left)
        elif not root.left and root.right:
            return self.summ(n, root.right)
        else:
            if not root.left.left and not root.left.right:
                return self.summ(n + root.left.val, root.right)
            else:
                return self.summ(n, root.left) + self.summ(0, root.right)
            
    
a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

s = Solution()
print(s.sumOfLeftLeaves(a))
