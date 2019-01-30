# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

k = 0

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



s = Solution()

r0 = TreeNode(3)

r10 = TreeNode(9)
r11 = TreeNode(20)

r20 = None
r21 = None
r22 = TreeNode(15)
r23 = TreeNode(7)

r0.left = r10
r0.right = r11

r10.left = r20
r10.right = r21
r11.left = r22
r11.right = r23

print(s.maxDepth(r0))
print(k)



