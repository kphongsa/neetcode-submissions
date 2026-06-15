# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1, l2 = list1, list2

        #base
        if (l1 is None):
            return l2
        if (l2 is None):
            return l1
            
        #let's recurse

        if (l1.val <= l2.val):
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
        else: 
            return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))