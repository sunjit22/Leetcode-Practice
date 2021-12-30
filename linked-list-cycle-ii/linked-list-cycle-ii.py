# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        hash_set = set()
        
        while(head):
            if head in hash_set:
                return head
            else:
                hash_set.add(head)
                
            head =head.next
        return None   