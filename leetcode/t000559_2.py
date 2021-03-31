
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        s = []
        if root:
            s.append((1, root))
        d = 0
        while s != []:
            cd, root = s.pop()
            if root:
                d = max(d, cd)
                for i in root.children:
                    s.append((cd + 1, i))

