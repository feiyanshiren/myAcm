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
                k.append(ListNode(head.val))
            head = head.next
        for i in range(1, len(k)):
            k[i - 1].next = k[i]
        return k[0] if len(k) != 0 else None
            
    

l = [1, 2, 6, 3, 4, 5, 6]
f = [ListNode(1)]
for i in range(1, len(l)):
    h = ListNode(l[i])
    f.append(h)
    f[i - 1].next = f[i]
s = Solution()
print(s.removeElements(f[0], 6))
        