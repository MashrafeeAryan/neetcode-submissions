# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        null -> head -> a -> b -> c -> null
        prev -> curr ->
        1. curr.next should point to prev: curr = prev
        2. curr should move ahead. curr = curr.next
        3. prev = curr
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
