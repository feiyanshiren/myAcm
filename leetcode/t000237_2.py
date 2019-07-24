# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if head.val == node.val:
            head.val = node.next.val
            head.next = node.next.next
        else:
            d = head
            while d.next:
                if d.next.val == node.val:
                    d.next = node.next
                    break
                else:
                    d = d.next
                    

    

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

s.deleteNode(head, head)
       
z = [head]
# c = []
while len(z) != 0:
    d = z.pop(0)
    # c.append(d.val)
    print(d.val)
    if d.next:
        z.append(d.next)

# print(c)

