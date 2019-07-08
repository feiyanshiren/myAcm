# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        k = []
        while head:
            if head.val != val:
                k.append(head.val)
            head = head.next
        if len(k) == 0:
            return None
        a = ListNode(k[0])
        b = a
        for i in range(1, len(k)):
            b.next = ListNode(k[i])
            b = b.next
        return a
            
    

l = [1, 2, 6, 3, 4, 5, 6]
f = [ListNode(1)]
for i in range(1, len(l)):
    h = ListNode(l[i])
    f.append(h)
    f[i - 1].next = f[i]
s = Solution()
print(s.removeElements(f[0], 6))
        