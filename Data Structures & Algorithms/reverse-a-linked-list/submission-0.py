# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        next_node = None
        if head == None:
            return None
        current_node = head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node
        return previous    