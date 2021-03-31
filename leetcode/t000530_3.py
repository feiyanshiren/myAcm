# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        r = 9223372036854775807
        l = self.f(root)
        print(l)
        for i in range(len(l) - 1):
            r = min(r, l[i + 1] - l[i])
        return r
    
    def f(self, root):
        if not root:
            return []
        return self.f(root.left) + [root.val] + self.f(root.right)
    
root = TreeNode(1)
r11 = TreeNode(3)
r21 = TreeNode(2)

root.right = r11
r11.left = r21
    
s = Solution()
print(s.getMinimumDifference(root))
