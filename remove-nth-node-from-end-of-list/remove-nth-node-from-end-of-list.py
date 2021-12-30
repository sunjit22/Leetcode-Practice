# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        count = 0 
        while curr is not None:
            count += 1
            curr = curr.next
        
        count -= n
        curr  = dummy 
        while (count > 0):
            curr = curr.next
            count -= 1
        
        curr.next = curr.next.next

        
        return dummy.next
        