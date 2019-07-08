# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
            
    

l = [1, 2, 6, 3, 4, 5, 6]
f = [ListNode(1)]
for i in range(1, len(l)):
    h = ListNode(l[i])
    f.append(h)
    f[i - 1].next = f[i]
s = Solution()
print(s.removeElements(f[0], 6))
        