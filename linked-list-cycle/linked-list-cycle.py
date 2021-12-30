# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False;
        
        track = set()
        while head is not None:
            if head in track:
                return True
            else:
                track.add(head)
            head = head.next     
        return False   

#         if head is None:
#                 return False
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if fast is None or fast.next is None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True
