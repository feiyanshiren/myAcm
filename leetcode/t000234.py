# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        a = [head.val]
        head = head.next
        while head:
            a.append(head.val)
            head = head.next
        l = len(a)
        if l == 1:
            return True
        b = l // 2
        if l % 2 == 0:
            return a[:b] == a[b:][::-1]
        else:
            return a[:b] == a[b + 1:][::-1]


a = [1, 2, 2, 2, 1]
b = [ListNode(a[0])]
for i in range(1, len(a)):
    b.append(ListNode(a[i]))
    b[i - 1].next = b[i]

   
s = Solution()
print(s.isPalindrome(b[0])) 