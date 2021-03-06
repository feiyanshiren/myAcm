# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        a = [[t1, t2]]
        while len(a) != 0:
            b = a.pop()
            if not b[0] or not b[1]:
                continue
            b[0].val += b[1].val
            if not b[0].left:
                b[0].left = b[1].left
            else:
                a.append([b[0].left, b[1].left])
            if not b[0].right:
                b[0].right = b[1].right
            else:
                a.append([b[0].right, b[1].right])


        return t1





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

t = s.mergeTrees(tt1[0], tt2[0])
a = [t]
while len(a) != 0:
    b = a.pop()
    print(b.val)
    if b.right:
        a.append(b.right)
    if b.left:
        a.append(b.left)