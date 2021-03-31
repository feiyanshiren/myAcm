# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
    

s = Solution()
a = [4, 5, 1, 9]

head = ListNode(a.pop(0))

z = [head]

while len(z) != 0:
    d = z.pop(0)
    if len(a) != 0:
        c = ListNode(a.pop(0))
        d.next = c
        z.append(c)

s.deleteNode(head.next)
       
z = [head]
c = []
while len(z) != 0:
    d = z.pop(0)
    c.append(d.val)
    print(d.val)
    if d.next:
        z.append(d.next)

print(c)

