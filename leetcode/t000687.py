# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.f(root)
        return self.res
    
    def f(self, t: TreeNode):
        if not t:
            return 0
        ll = self.f(t.left)
        rl = self.f(t.right)
        l = 0
        r = 0
        if t.left and t.left.val == t.val:
            l = ll + 1
        if t.right and t.right.val == t.val:
            r = rl + 1
        self.res = max(self.res, l + r)
        return max(l, r)
            
    
s = Solution()

t1 = [TreeNode(5), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(1), TreeNode(5)]
t1[0].left = t1[1]
t1[0].right = t1[2]
t1[1].left = t1[3]
t1[1].right = t1[4]
t1[2].right = t1[5]

print(s.longestUnivaluePath(t1[0]))

t2 = [TreeNode(5), TreeNode(4), TreeNode(5), TreeNode(4), TreeNode(4), TreeNode(5)]
t2[0].left = t2[1]
t2[0].right = t2[2]
t2[1].left = t2[3]
t2[1].right = t2[4]
t2[2].right = t2[5]

print(s.longestUnivaluePath(t2[0]))