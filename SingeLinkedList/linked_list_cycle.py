# TODO: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        s_node = head
        f_node = head
        while f_node.next and f_node.next.next:
            s_node = s_node.next
            f_node = f_node.next.next
            if s_node == f_node:
                return True
        return False