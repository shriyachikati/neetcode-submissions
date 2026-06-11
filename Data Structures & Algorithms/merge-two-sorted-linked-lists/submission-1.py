# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy to make sure we have reference to the original head
        dummy = head = ListNode()

        # Keep adding nodes to the head while the two lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            # Change the current head
            head = head.next

        # Add the remaining nodes of either of the lists to the head
        head.next = list1 or list2

        # Since head has moved to the end, return dummy.next which is our output
        return dummy.next