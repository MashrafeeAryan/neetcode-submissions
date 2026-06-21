# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        Brute force
        1. while l1 and l2 are not null:
        2. if l1.val < l2.val:
            3. head.next = l1
            4. move the l1 = l1.next
        3. if l2.val <= l1.val:
            3. head.next = l2.val
            4. move the l2 = l2.next
        5. if l1:
            tail.next = l1
        6. if l2:
            tail.next = l2
        
        return newListNode.next

        """
        newLinkedList = ListNode()
        head = newLinkedList
     
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return newLinkedList.next