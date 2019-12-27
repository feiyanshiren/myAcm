# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        a = self.f(t1)
        b = self.f(t2)
        print(a)
        print(b)
        la = len(a)
        lb = len(b)
        if la > lb:
            for i in range(lb):
                if a[i] and b[i]:
                    a[i] += b[i]
                if not a[i] and b[i]:
                    a[i] = b[i]
        else:
            for i in range(la):
                if b[i] and a[i]:
                    b[i] += a[i]
                if not b[i] and a[i]:
                    b[i] = a[i]
            a = b[:]
        print(a)
        if len(a) == 0:
            return None
        else:
            d = a.pop(0)
            if d:
                t = TreeNode(d)
                z = [t]
                while len(z) != 0:
                    h = z.pop(0)
                    if h:
                        if len(a) != 0:
                            d = a.pop(0)
                            if d:
                                h.left = TreeNode(d)
                            z.append(h.left)
                        if len(a) != 0:
                            d = a.pop(0)
                            if d:
                                h.right = TreeNode(d)
                            z.append(h.right)
                return t
            else:
                return None

    def f(self, t1: TreeNode):
        a = [t1]
        c = []
        while len(a) != 0:
            b = a.pop(0)
            if b:
                c.append(b.val)
                if not b.left and not b.right:
                    continue
                a.append(b.left)
                a.append(b.right)
            else:
                c.append(None)
        return c
            



t1 = TreeNode(1)
t13 = TreeNode(3)
t12 = TreeNode(2)
t15 = TreeNode(5)

t1.left = t13
t1.right = t12
t13.left = t15

t2 = TreeNode(2)
t21 = TreeNode(1)
t23 = TreeNode(3)
t24 = TreeNode(4)
t27 = TreeNode(7)

t2.left = t21
t2.right = t23
t21.right = t24
t23.right = t27



s = Solution()
t = s.mergeTrees(t1, t2)
a = [t]
while len(a) != 0:
    b = a.pop()
    print(b.val)
    if b.right:
        a.append(b.right)
    if b.left:
        a.append(b.left)

tt = s.mergeTrees(None, None)
print(tt)

tt1 = [TreeNode(1), TreeNode(2), TreeNode(3)]
tt2 = [TreeNode(1), TreeNode(2), TreeNode(3)]
tt1[0].left = tt1[1]
tt1[1].left = tt1[2]

tt2[0].right = tt2[1]
tt2[1].right = tt2[2]

s.mergeTrees(tt1[0], tt2[0])