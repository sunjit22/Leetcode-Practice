# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        start = head
        length = 1
        
        # Close linked list to a ring
        while start.next:
            length+=1
            start = start.next
        
        start.next = head
        
        # find new tail
        first = divmod(k,length)[1]
        
        n = length - first
        start_2 = head
        for i in range(1,n):
            start_2 = start_2.next
        new_head = start_2.next    
        start_2.next =None   

        return new_head  