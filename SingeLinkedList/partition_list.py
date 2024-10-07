from typing import Optional

# https://leetcode.com/problems/partition-list/description/

#  dummy head node is most important for linkedi list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast.next:
            if fast.next.val >= x:
                fast = fast.next
            else:
                # remove the next node < x
                tmp = fast.next
                fast.next = fast.next.next
                # insert the node after slow ptr
                tmp_next = slow.next
                slow.next = tmp
                tmp.next = tmp_next
                # move forward the slow and fast ptr
                slow = slow.next
                fast = slow

        return dummy.next
