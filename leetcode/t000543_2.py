# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1
        def d(t):
            if not t:
                return 0
            l = d(t.left)
            r = d(t.right)
            self.res = max(self.res, l + r + 1)
            return max(l, r) + 1
        
        d(root)
        return self.res - 1

root = TreeNode(1)
r11 = TreeNode(2)
r12 = TreeNode(3)
r21 = TreeNode(4)
r22 = TreeNode(5)
r31 = TreeNode(5)
r32 = TreeNode(5)
r41 = TreeNode(5)
r42 = TreeNode(5)

root.left = r11
root.right = r12

r11.left = r21
r11.right = r22

r21.left = r31
r22.left = r32

r31.left = r41
r32.left = r42

s = Solution()
print(s.diameterOfBinaryTree(root))
