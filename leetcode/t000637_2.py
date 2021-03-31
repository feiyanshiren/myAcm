from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        s = []
        c = []
        self.f(root, 0, s, c)
        for i in range(len(s)):
            s[i] = s[i] / c[i]
        return s

    def f(self, t: TreeNode, h: int, s: List, c: List):
        if not t:
            return
        if h < len(s):
            s[h] = s[h] + t.val
            c[h] = c[h] + 1
        else:
            s.append(1.0 * t.val)
            c.append(1)
        self.f(t.left, h + 1, s, c)
        self.f(t.right, h + 1, s, c)


t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15 = TreeNode(15)
t7 = TreeNode(7)
t8 = TreeNode(8)

t3.left = t9
t3.right = t20
t20.left = t15
t20.right = t7
t9.left = t8

s = Solution()

print(s.averageOfLevels(t3))

