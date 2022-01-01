# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0);
    
        curr = dummyHead;
        carry = 0;
        
        # Iterate until one of the list exists
        while l1 or l2:
            v1 = 0
            v2 = 0
            if(l1):
                v1 = l1.val
                l1 = l1.next
                
            if(l2):
                v2 = l2.val
                l2 = l2.next    
            
            sum = v1 + v2 + carry
            
            carry, val = divmod(sum, 10)
            
            curr.next = ListNode(val);
            curr = curr.next
            
        # Edge case: Add carry in the end if no number left      
        if(carry > 0):
            curr.next = ListNode(carry)
        
        return dummyHead.next;    
            
            