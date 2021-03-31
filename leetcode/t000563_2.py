# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.r = 0
        self.f(root)
        return self.r
    
    def f(self, node):
        if not node:
            return 0
        else:
            l = self.f(node.left)
            r = self.f(node.right)
            self.r += abs(l - r)
            return node.val + l + r
    
  
  
root = TreeNode(1)          
r11 = TreeNode(2)          
r12 = TreeNode(3)          
r21 = TreeNode(4)          
root.left = r11
root.right = r12
r11.left = r21
    
s = Solution()
print(s.findTilt(root))    

            
    
    