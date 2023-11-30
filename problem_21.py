from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode()
        prev = list3

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        if not list1:
            prev.next = list2

        if not list2:
            prev.next = list1

        return list3.next


# first list [1, 2, 3]
head1 = ListNode(val=1)
node1_2 = ListNode(val=2)
node1_3 = ListNode(val=4)

head1.next = node1_2
node1_2.next = node1_3

# second list [1, 3, 4]
head2 = ListNode(val=1)
node2_2 = ListNode(val=3)
node2_3 = ListNode(val=4)

head2.next = node2_2
node2_2.next = node2_3


sol = Solution()
sol.mergeTwoLists(list1=head1, list2=head2)
