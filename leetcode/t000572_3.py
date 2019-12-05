
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
                    
    
    def isSame(self,s,t):
        if s and t:
            return s.val==t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
        elif s==t:
            return True
        else:
            return False


s1 = TreeNode(3)
t1 = TreeNode(4)

s11 = TreeNode(4)
s12 = TreeNode(5)

s21 = TreeNode(1)
s22 = TreeNode(2)

s31 = TreeNode(0)

t11 = TreeNode(1)
t12 = TreeNode(2)

s1.left = s11
s1.right = s12

s11.left = s21
s11.right = s22

s22.left = s31

t1.left = t11
t1.right = t12

s = Solution()
print(s.isSubtree(s1, t1))