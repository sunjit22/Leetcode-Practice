# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iter = head
        len = 0
        i = 0
        while(iter):
            iter = iter.next
            len += 1
            
        if(len == n):
            return head.next
        
        iter = head 
        for i in range(1, len-n):
            iter = iter.next
            
        iter.next = iter.next.next
        return head
        