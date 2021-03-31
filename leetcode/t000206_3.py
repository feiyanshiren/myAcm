# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        p = None
        c = head
        while c:
            t = None
            if c.next:
                t = ListNode(c.next.val)
                t.next = c.next,next
            c.next = p
            p = c
            c = t
        return p
    

a = [1, 2, 3, 4, 5]
b = [ListNode(1)]
for i in range(1, len(a)):
    b.append(ListNode(a[i]))
    b[i - 1].next = ListNode(a[i])
    

s = Solution()
print(s.reverseList(b[0]))