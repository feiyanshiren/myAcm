from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        a = []
        if not root:
            return a
        b = [root]
        while len(b) != 0:
            c = b.pop()
            if c:
                a.append(c.val)
            if c.children:
                b += c.children[::-1]
        return a

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.children = [n3, n2, n4]
n3.children = [n5, n6]

s = Solution()
print(s.preorder(n1))
