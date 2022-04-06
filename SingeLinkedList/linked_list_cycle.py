# TODO: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def get_head(self):
        return self.head 
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def insert_at_head(self, value:float):
        if self.is_empty():
            self.head = Node(value)
        else:
            temp_node = Node(value)
            temp_node.next = self.head
            self.head = temp_node
        return self
    
    def insert_at_tail(self, value: float):
        current = self.get_head()
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        return self
    
    
    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None
        

class Solution:
    def hasCycle(self, head: Node) -> bool:
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