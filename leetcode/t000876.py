


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l1 = [head]
        l2 = []
        while l1:
            h1 = l1.pop()
            l2.append(h1)
            if h1.next:
                l1.append(h1.next)
        m = len(l2) // 2
        return l2[m]





class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k, cur = 0, head
        while k < n // 2:
            k += 1
            cur = cur.next
        return cur


# ```
# ---
#
# 876.
# 链表的中间结点 - -3
#
# 给定一个带有头结点
# head
# 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#
#
# 示例
# 1：
#
# 输入：[1, 2, 3, 4, 5]
# 输出：此列表中的结点
# 3(序列化形式：[3, 4, 5])
# 返回的结点值为
# 3 。 (测评系统对该结点序列化表述是[3, 4, 5])。
# 注意，我们返回了一个
# ListNode
# 类型的对象
# ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及
# ans.next.next.next = NULL.
#
# 示例
# 2：
#
# 输入：[1, 2, 3, 4, 5, 6]
# 输出：此列表中的结点
# 4(序列化形式：[4, 5, 6])
# 由于该列表有两个中间结点，值分别为
# 3
# 和
# 4，我们返回第二个结点。
#
#
#
# 提示：
#
# 给定链表的结点数介于
# 1
# 和
# 100
# 之间。
#
# 解：
# 快慢指针
# 我们可以继续优化方法二，用两个指针
# slow
# 与
# fast
# 一起遍历链表。slow
# 一次走一步，fast
# 一次走两步。那么当
# fast
# 到达链表的末尾时，slow
# 必然位于中间。
#
#
# ```py


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

