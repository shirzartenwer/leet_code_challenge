# https://neetcode.io/problems/remove-node-from-end-of-linked-list

# BruteForce Solution


from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return

        cur = head
        nodes = []

        while cur:
            nodes.append(cur)
            cur = cur.next

        remove_index = len(nodes) - n

        if remove_index == 0:
            return head.next

        nodes[remove_index-1].next = nodes[remove_index].next
        return head


# Two Poitner solution: right pointer is exactly n+1 position right to the left pointer
class TPSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return

        dummy = ListNode()
        dummy.next = head

        left = dummy

        for i in range(n):
            head = head.next

        right = head

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
