# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = head
        carry = 0
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            carry, value = divmod(sum_,10)
            new_node = ListNode(value)
            head.next = new_node
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                sum_ = l1.val + carry
                carry, value = divmod(sum_,10)
                new_node = ListNode(value)
                head.next = new_node
                head = head.next
                l1 = l1.next
        if l2:
            while l2: 
                sum_ = l2.val + carry
                carry, value = divmod(sum_,10)
                new_node = ListNode(value)
                head.next = new_node
                head = head.next
                l2 = l2.next
        if carry > 0:
            head.next = ListNode(carry,None)
            
        return result.next     
            
            