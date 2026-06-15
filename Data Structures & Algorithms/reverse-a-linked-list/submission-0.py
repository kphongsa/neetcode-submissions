# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        rest = None

        if (curr is not None):
            rest = curr.next

        while (curr is not None):
            curr.next = prev

            prev = curr
            curr = rest
            
            if (rest is not None):
                rest = rest.next

        return prev
            


        

        