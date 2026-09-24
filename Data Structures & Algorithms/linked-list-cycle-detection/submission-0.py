# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
            if head in node_list:
                return True
        return False