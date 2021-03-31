# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s1 = [s]
        r1 = []
        while len(s1) != 0:
            s2 = s1.pop(0)
            ss = []
            self.f(s2, ss)
            r1.append(ss)
            if s2.left:
                s1.append(s2.left)
            if s2.right:
                s1.append(s2.right)

        print(r1)
        r2 = []
        self.f(t, r2)

        print(r2)
        if r2 in r1:
            return True
        return False


    def f(self, r, l):
        if not r:
            return
        else:
            l.append(r.val)
            if r.left:
                self.f(r.left, l)
            else:
                l.append("lnull")
            if r.right:
                self.f(r.right, l)
            else:
                l.append("rnull")


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