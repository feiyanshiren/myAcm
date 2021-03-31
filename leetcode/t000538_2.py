# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.s = 0
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.f1(root)
        return root
        
    def f1(self, root):
        if root:
            self.f1(root.right)
            self.s += root.val
            root.val = self.s
            self.f1(root.left)

root = TreeNode(5)
r11 = TreeNode(2)
r12 = TreeNode(13)
root.left = r11
root.right = r12


s = Solution()
print(s.convertBST(root))