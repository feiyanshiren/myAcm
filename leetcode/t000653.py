# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a = [root]
        b = []
        while len(a) != 0:
            c = a.pop(0)
            if c:
                b.append(c.val)
                if c.left:
                    a.append(c.left)
                if c.right:
                    a.append(c.right)
        if b == []:
            return False
        else:
            for i in range(len(b)):
                d = b.pop(i)
                e = k - d
                if e in b:
                    return True
                else:
                    b.insert(i, d)
            return False

                



s = Solution()

t = [0 for i in range(12)]
t[0] = TreeNode(5)
t[1] = TreeNode(3)
t[0].left = t[1]
t[2] = TreeNode(6)
t[0].right = t[2]
t[3] = TreeNode(2)
t[1].left = t[3]
t[4] = TreeNode(4)
t[1].right = t[4]
t[5] = TreeNode(7)
t[2].right = t[5]


t[6] = TreeNode(5)
t[7] = TreeNode(3)
t[6].left = t[7]
t[8] = TreeNode(6)
t[6].right = t[8]
t[9] = TreeNode(2)
t[7].left = t[9]
t[10] = TreeNode(4)
t[7].right = t[10]
t[11] = TreeNode(7)
t[8].right = t[11]

print(s.findTarget(t[0], 9))
print(s.findTarget(t[6], 28))