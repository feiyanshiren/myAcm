# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        return self.f(root)
    
    def f(self, node):
        if not node:
            return 0
        else:
            if not node.left and not node.right:
                return 0
            else:
                l = self.k(node.left)
                r = self.k(node.right)
                return abs(l - r) + self.f(node.left) + self.f(node.right)
    
    def k(self, node):
        if not node:
            return 0
        else:
            return node.val + self.k(node.left) + self.k(node.right)
  
  
root = TreeNode(1)          
r11 = TreeNode(2)          
r12 = TreeNode(3)          
r21 = TreeNode(4)          
root.left = r11
root.right = r12
r11.left = r21
    
s = Solution()
print(s.findTilt(root))    

            
    
    