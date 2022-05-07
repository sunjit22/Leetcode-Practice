# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If linked list is empty
        prev = None
        curr = head
        
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        
       
        
#         if not head:
#             return None
#         else:
#             prev = None
#             curr = head
#             follow = curr.next
#             while curr != None:
#                 curr.next = prev
#                 prev = curr
#                 curr = follow
#                 if follow:
#                     follow = follow.next
#             return prev
        
        