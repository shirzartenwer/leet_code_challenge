# https://neetcode.io/problems/add-two-numbers
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        carrying_sum = 0

        result_dummy = ListNode()
        result_head = result_dummy.next = ListNode(0, None)

        while cur1 or cur2:
            if cur1 is None:
                cur_sum = cur2.val + carrying_sum
                cur2 = cur2.next
            elif cur2 is None:
                cur_sum = cur1.val + carrying_sum
                cur1 = cur1.next
            else:
                cur_sum = cur1.val + cur2.val + carrying_sum
                cur1 = cur1.next
                cur2 = cur2.next

            if cur_sum >= 10:
                carrying_sum = 1
                result_head.val = cur_sum - 10
            else:
                carrying_sum = 0
                result_head.val = cur_sum

            if cur1 is not None or cur2 is not None or carrying_sum != 0:
                result_head.next = ListNode(carrying_sum, None)
                result_head = result_head.next

        return result_dummy.next
