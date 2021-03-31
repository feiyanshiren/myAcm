from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        a = []
        self.f(root, a)
        return a

    def f(self, node: "Node", l: List):
        if not node:
            return
        else:
            l.append(node.val)
            if node.children:
                for i in node.children:
                    self.f(i, l)

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
