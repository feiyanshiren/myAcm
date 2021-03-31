# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        a = [head.val]
        while head.next:
            head = head.next
            a.append(head.val)
        a = a[::-1]
        b = [ListNode(a[0])]
        for i in range(1, len(a)):
            b.append(ListNode(a[i]))
            b[i - 1].next = b[i]
        return b[0]
    

a = [1, 2, 3, 4, 5]
b = [ListNode(1)]
for i in range(1, len(a)):
    b.append(ListNode(a[i]))
    b[i - 1].next = ListNode(a[i])
    

s = Solution()
print(s.reverseList(b[0]))