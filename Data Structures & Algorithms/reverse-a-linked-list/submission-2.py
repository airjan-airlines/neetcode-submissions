# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return the first node in the linked list
        # could just iterate through and swap the links
        if head is None:
            return None
        if head.next is None:
            return head

        lag_node = None

        while head:
            new = head.next
            head.next = lag_node
            lag_node = head
            head = new

        return lag_node


