# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        z = [t]
        s = ""
        while len(z) != 0:
            t1 = z.pop()
            if t1 == "(" or t1 == ")":
                s += t1
                continue
            elif t1:
                if t1.right:
                    z.append(")")
                    z.append(t1.right)
                    z.append("(")
                    z.append(")")
                    z.append(t1.left)
                    z.append("(")
                elif t1.left and not t1.right:
                    z.append(")")
                    z.append(t1.left)
                    z.append("(")
                s += str(t1.val)
        return s


r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)

r1.left = r2
r1.right = r3
r2.left = r4

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)

t1.left = t2
t1.right = t3
t2.right = t4


s = Solution()
print(s.tree2str(r1))
print(s.tree2str(t1))