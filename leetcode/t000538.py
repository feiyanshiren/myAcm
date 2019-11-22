# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        a = self.f(root)
        b = {}
        for i in range(len(a)):
            b[a[i]] = sum(a[i:])
        self.f1(root, b)
        return root
        
    def f1(self, root, b):
        if root:
            root.val = b.get(root.val)
            self.f1(root.left, b)
            self.f1(root.right, b)
    
    def f(self, root):
        if not root:
            return []
        else:
            return self.f(root.left) + [root.val] + self.f(root.right)
    


root = TreeNode(5)
r11 = TreeNode(2)
r12 = TreeNode(13)
root.left = r11
root.right = r12


s = Solution()
print(s.convertBST(root))