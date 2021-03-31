# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        a = [root]
        while len(a) != 0:
            b = a.pop()
            z = 0
            y = 0
            if b and b.left:
               z = self.f(b.left)
               a.append(b.left)        
            else:
                z = 0
            if b and b.right:
                y = self.f(b.right)
                a.append(b.right)   
            else:
                y = 0
            res  = max(z + y, res)
        return res
    
    def f(self, root):
        if not root:
            return 0
        l = self.f(root.left)
        r = self.f(root.right)
        if l > r:
            return l + 1
        else:
            return r + 1

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
