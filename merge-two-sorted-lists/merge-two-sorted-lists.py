# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        l1_head = l1
        l2_head = l2
        result_node = ListNode(-1)
        new_node = result_node
        while l1_head and l2_head:
            if l1_head.val <= l2_head.val:
                new_node.next = l1_head
                l1_head = l1_head.next
            else:
                new_node.next = l2_head
                l2_head = l2_head.next
            new_node = new_node.next     
        while l1_head:
            new_node.next = l1_head
            l1_head = l1_head.next
            new_node = new_node.next 
            
        while l2_head:
            new_node.next = l2_head
            l2_head = l2_head.next   
            new_node = new_node.next 
            
        return result_node.next     
                
        
        