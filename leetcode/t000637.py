from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        a = [[root]]
        r = []
        while len(a) != 0:
            b = a.pop(0)
            l = len(b)
            if l > 0:
                s = 0
                for i in b:
                    s += i.val
                r.append(s / l)
            else:
                break
            for i in b:
                if i.left:
                    if len(a) == 0:
                        a.append([i.left])
                    else:
                        a[0].append(i.left)
                if i.right:
                    if len(a) == 0:
                        a.append([i.right])
                    else:
                        a[0].append(i.right)
        return r


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

