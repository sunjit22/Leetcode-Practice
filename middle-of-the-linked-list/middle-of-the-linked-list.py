# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        mid = count//2 + 1
        
        for i in range(1,mid):
            head = head.next
            
        return head    
            