from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            head = None
            return head

        pos = length - n
        idx = 0

        prev = None
        curr = head

        while idx != pos:
            idx += 1
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        return head


head = ListNode(1)
head.next = ListNode(2)


sol = Solution()

print(sol.removeNthFromEnd(head, 2))
